import numpy as np
from numpy import linalg as LA
import cv2
# iniciar con un resel

class CarDCENV(object):
	n_sensor = 8
	action_dim = 1
	state_dim = n_sensor + 1
	state_dim_ = 6
	viewer = None
	sensor_max = 150
	#start_point = [50, 50]
	dt = 0.1
	speed = 40.
	def __init__(self, map_bin,goald,start_point):
		d = pow(2,0.5)/2
		self.kernel_s = np.array([[1,0],[d,d],[0,1],[-d,d],[-1,0],[-d,-d],[0,-1],[d,-d]],dtype=np.float64)
		self.start_point = start_point
		self.goald = goald
		self.action_bound = [-1, 1]
		self.mapa = map_bin
		self.window = [map_bin.shape[1], map_bin.shape[0]] # (X , Y)
		self.car_info = np.array([0, 0, 0], dtype=np.float64)
		self.sensor_info = self.sensor_max + np.zeros((self.state_dim)) 
		self.sensor_info[0] = 1
		self.terminal = False
		self.exit = False
		self.fail = False
		self.dist_i = np.array([self.goald[0]-self.start_point[0] , self.goald[1]-self.start_point[1]])
		self.last_dist= LA.norm(self.dist_i)
		self.temp_map = self.mapa.copy()
		self.last_r = 0
		self.last_s = 0

	def step(self, action):
		cx3, cy3, _ = self.car_info.copy()
		action = np.clip(action, *self.action_bound)[0]
		self.car_info[2] += action * np.pi/30 # Max 6 degrees
		self.car_info[:2] = self.car_info[:2] + self.speed * self.dt * np.array([np.cos(self.car_info[2]), np.sin(self.car_info[2])])
		self._update_sensor()
		s = self._get_state()
		dd = np.array([self.goald[0] - cx3 , self.goald[1] - cy3])
		dd_n = LA.norm(dd)
		if self.exit:
			r = 1
		elif self.fail:
			r = self.last_r
			s = self.last_s
		elif self.terminal:
			r = -1
		else:
			#r = 1 - (1+s[0])*pow(dd_n/self.last_dist,4)*0.8
			r = 0.4 + (0.2 if s[0]<1 else 0.001) + (0.4 if dd_n/self.last_dist<1 else 0.001)
			self.last_r = r
			self.last_s = s
			if dd_n/self.last_dist<1:
				self.last_dist = dd_n
		#elif dd_n/self.last_dist<1:
		#	r = 1 #- 0.99*pow(LA.norm(dd)/self.last_dist,3)
		#	self.last_dist = LA.norm(dd)
		return s,r,self.terminal,self.exit


	def reset(self):
		self.terminal = False
		self.exit = False
		self.fail = False
		self.last_dist= LA.norm(self.dist_i)
		self.car_info = np.array([0, 0, 0], dtype=np.float64)
		self.car_info = np.array([*self.start_point, np.pi/2])
		self._update_sensor() # solo
		self.temp_map = self.mapa.copy()
		cv2.circle(self.temp_map, (int(round(self.goald[0])),int(round(self.goald[1]))), 30, (255, 0, 0), 1)
		return self._get_state()

	def render(self):
	  	cx2, cy2, _ = self.car_info.copy()
	  	if not self.terminal:
	  		cv2.circle(self.temp_map, (int(round(cx2)),int(round(cy2))), 5, (255, 0, 0), -1)
	  	return self.temp_map

	def _get_state(self):
	  	cx1, cy1, _ = self.car_info.copy()
	  	#s = np.array([self.sensor_info[i]/round(self.sensor_max*1.42) if i%2 else self.sensor_info[i]/round(self.sensor_max) for i in range(1,self.state_dim)])
	  	s0 = self.sensor_info[0].copy()
	  	s = self.sensor_info/round(self.sensor_max)
	  	s[0] = s0
	  	#dd = np.array([self.goald[0] - cx1 , self.goald[1] - cy1])
	  	#dist_math = LA.norm(dd)/LA.norm(self.dist_i)
	  	#s[0] = dist_math
	  	s = np.array([s[i] for i in (-2,-1,1,2,3,0)])
	  	return s

	def _update_sensor(self):
	  	cx, cy, rotation = self.car_info.copy()
	  	if not(np.isnan(cx) or np.isnan(cy)):
	  		dx = self.goald[0]-cx
	  		dy = self.goald[1]-cy
		  	self.sensor_info = self.sensor_max + np.zeros((self.state_dim)) 
		  	kernel_s_rot = self.kernel_s.copy()
		  	kernel_s_temp = self.kernel_s.copy()
		  	kernel_s_rot[:,0] =  kernel_s_temp[:,0]*np.cos(rotation) - kernel_s_temp[:,1]*np.sin(rotation)
		  	kernel_s_rot[:,1] =  kernel_s_temp[:,0]*np.sin(rotation) + kernel_s_temp[:,1]*np.cos(rotation)
		  	#kernel_s_cur = self.kernel_s + [cx+cy]
		  	#kernel_s_rot = self.kernel_s ###############################################################

		  	# Midiendo distancias con los obstaculos y a la ventana
		  	for i in range(1,self.sensor_max+1):
		  		kernel_s_cur = kernel_s_rot*i + [cx,cy]
		  		L=[]                
		  		for sensor_n in range(len(kernel_s_cur)):
		  			# Distancia a los obstaculos
		  			if 0<round(kernel_s_cur[sensor_n][1])<self.window[1] and 0<round(kernel_s_cur[sensor_n][0])<self.window[0]:
			  			if self.mapa[int(round(kernel_s_cur[sensor_n][1])),int(round(kernel_s_cur[sensor_n][0]))]==255: # se invierte el orden de X,Y a Y,X, debido a que map es una matriz
			  				dist = np.array([kernel_s_cur[sensor_n][0]-cx,kernel_s_cur[sensor_n][1]-cy])
			  				norm_dist = LA.norm(dist)                        
			  				if self.sensor_info[sensor_n+1] > norm_dist:
			  					self.sensor_info[sensor_n+1] = norm_dist
			  		# Distancia a los límites de la ventana
			  		else:
			  			px = np.clip(kernel_s_cur[sensor_n][0],0,self.window[0])
			  			py = np.clip(kernel_s_cur[sensor_n][1],0,self.window[1])
			  			dist = np.array([px-cx,py-cy])
			  			norm_dist = LA.norm(dist)
			  			if self.sensor_info[sensor_n+1] > norm_dist:
			  				self.sensor_info[sensor_n+1] = norm_dist
                            
			  		dist_gl = np.array([kernel_s_cur[sensor_n][0]-self.goald[0],kernel_s_cur[sensor_n][1]-self.goald[1]])                   
			  		norm_dist_gl = LA.norm(dist_gl)
			  		L.append(norm_dist_gl)
		  	weight = [1,0.75,0.5,0.25,0]
		  	ind = np.argmin(np.array([L[i] for i in (-2,-1,0,1,2)]))
		  	self.sensor_info[0]  = weight[ind]                  

			# Comprobando colisión con ventana
		  	if not (0<int(round(cx))<self.window[0] and 0<int(round(cy))<self.window[1]):
		  		self.terminal = True
		  		#self.sensor_info = np.zeros((self.state_dim)) 

		  	# Comprobando colisión con obstaculo
		  	elif self.mapa[int(round(cy)),int(round(cx))] == 255:
		  		self.terminal = True
		  		#self.sensor_info = np.zeros((self.state_dim)) 

		  	# Comprobando si llegó al objetivo
		  	elif abs(dx)<30 and abs(dy)<30:
		  		self.terminal = True
		  		self.exit = True
	  	else:
	  		print("Fail in the cx cy")
	  		self.fail = True
	  		self.terminal = True
