from manimlib.imports import *
import numpy as np

class mx_axis(LinearTransformationScene):
   	def construct(self):
            matrix = [[1, 0], 
                      [0, -1]]
            def f(x):
            	    return 0
            graph=FunctionGraph(f,x_min=-7,x_max=7)
            self.add_transformable_mobject(graph)
            
            vector = np.array([3,2,0])
            object = Dot()
            object.move_to(vector)
            object_2 = object
            self.add(object_2)
            self.add_transformable_mobject(object)
            
            self.apply_matrix(matrix)
            self.wait()
            
class my_x(LinearTransformationScene):
   	def construct(self):
            matrix = [[0, 1], 
                      [1, 0]]
            def f(x):
            	    return x
            graph=FunctionGraph(f,x_min=-7,x_max=7)
            self.add_transformable_mobject(graph)
            
           # vector = np.array([3,2,0])
           # object = Dot()
           # object.move_to(vector)
            self.add_transformable_mobject(Dot(np.array([3,1,0]),fill_color=RED, fill_opacity=1, color=RED))
            self.add(Dot(np.array([3,1,0]),fill_color=RED, fill_opacity=0.5, color=RED))
            A = TextMobject("$$A$$")
            A.move_to(np.array([3.5,1.5,0]))
            self.add(A)
           # self.add()
           # self.add_transformable_mobject(object)
            
            self.apply_matrix(matrix)
            
            A_img = TextMobject("$$A^\prime$$")
            A_img.move_to(np.array([0.5,3.5,0]))
            self.play(Write(A_img))
            
            self.wait()
            
class my_nx(LinearTransformationScene):
   	def construct(self):
            matrix = [[0, -1], 
                      [-1, 0]]
            def f(x):
            	    return -x
            graph=FunctionGraph(f,x_min=-7,x_max=7)
            self.add_transformable_mobject(graph)
            
            vector = np.array([2,3,0])
            object = Dot()
            object.move_to(vector)
            object2 = object
            self.add(object2)
            self.add_transformable_mobject(object)
            
            self.apply_matrix(matrix)
            self.wait()
            
class rcw90(LinearTransformationScene):
   	def construct(self):
            matrix = [[0, 1], 
                      [-1, 0]]
        
           # def f(x):
           # 	    return -x
           # graph=FunctionGraph(f,x_min=-7,x_max=7)
           # self.add_transformable_mobject(graph)
            

           # triangle = Polygon(np.array([1,1,0]),np.array([2,3,0]),np.array([2,1,0]),fill_color=RED, fill_opacity=0.9, color=RED)
           # object = Triangle(fill_color=GOLD_B, fill_opacity=1, color=GOLD_A)
           # object.move_to(vector)
           # self.add(triangle)
            
            self.add_transformable_mobject(Polygon(np.array([1,1,0]),np.array([2,3,0]),np.array([2,1,0]),fill_color=RED, fill_opacity=1, color=RED))
            A = TextMobject("$$A$$")
            A.move_to(np.array([2.5,3.5,0]))
            self.add(A)
            
            self.add(Polygon(np.array([1,1,0]),np.array([2,3,0]),np.array([2,1,0]),fill_color=RED, fill_opacity=0.5, color=RED))
            self.apply_matrix(matrix)
            A_img = TextMobject("$$A^\prime$$")
          #  A_img.move_to(np.dot(matrix,vector))
            A_img.move_to(np.array([3.5,-1.5,0]))
            self.play(Write(A_img))
            self.wait()
                   
            
class test(Scene):
   def construct(self):
        vector = np.array([3,1,0])
        object = Dot()
        object.move_to(vector)
        self.add(object)
        
        
        self.wait()
        
class Intro(LinearTransformationScene):
  def construct(self):
    name = TextMobject("Awab Qureshi")
    name.move_to(np.array([-5.5, -3.5, 0]))
    self.add(name)
    
    T = TextMobject("Translation")
    T.move_to(np.array([-5.5, 2.5, 0]))
    self.play(Write(T))
    tri = Polygon(np.array([-1,3,0]),np.array([-1,1,0]),np.array([-2,1,0]),fill_color=RED, fill_opacity=1, color=RED)
    self.play(Write(tri))
    self.play(ApplyMethod(tri.shift,np.array([3,-4,0])))
    self.wait()
    self.play(FadeOut(tri))
    
    
    
    M = TextMobject("Reflection")
    M.move_to(np.array([-5.5, 2.5, 0]))
   # self.play(Write(M))
    self.play(Transform(T,M))
    
    m_matrix = [[0, 1], 
                [1, 0]]
    def f(x):
          return x
    graph=FunctionGraph(f,x_min=-7,x_max=7)
    self.play(Write(graph))
    
    # vector = np.array([3,2,0])
    # object = Dot()
    # object.move_to(vector)
    
    A = TextMobject("$$A$$")
    A.move_to(np.array([3.5,1.5,0]))
    self.play(Write(A))
    
    dot_1 = Dot(np.array([3,1,0]),fill_color=RED, fill_opacity=1, color=RED)
    dot_2 = Dot(np.array([3,1,0]),fill_color=RED, fill_opacity=0.5, color=RED)
    self.add_transformable_mobject(dot_1)
    self.add(dot_2)
    # self.add()
    # self.add_transformable_mobject(object)
    self.wait()
    self.apply_matrix(m_matrix)
    
    A_img = TextMobject("$$A^\prime$$")
    A_img.move_to(np.array([0.5,3.5,0]))
    self.play(Write(A_img))
    self.wait()
    self.play(FadeOut(A), FadeOut(A_img), FadeOut(dot_1), FadeOut(dot_2), FadeOut(graph))
    
    
    
    R = TextMobject("Rotation")
    R.move_to(np.array([-5.5, 2.5, 0]))
    self.play(Transform(T,R))
    r_matrix = [[0, 1], 
                [-1, 0]]
    
    self.add_transformable_mobject(Polygon(np.array([1,1,0]),np.array([2,3,0]),np.array([2,1,0]),fill_color=RED, fill_opacity=1, color=RED))
    A = TextMobject("$$A$$")
    A.move_to(np.array([2.5,3.5,0]))
    self.play(Write(A))
    self.add(Dot(np.array([1,3,0]),fill_color=RED,fill_opacity=0.5,color=RED))
    
    self.add(Polygon(np.array([1,1,0]),np.array([2,3,0]),np.array([2,1,0]),fill_color=RED, fill_opacity=0.5, color=RED))
    self.apply_matrix(r_matrix)
    A_img = TextMobject("$$A^\prime$$")
  #  A_img.move_to(np.dot(matrix,vector))
    A_img.move_to(np.array([3.5,-1.5,0]))
    self.play(Write(A_img))
    self.wait()
    
class r_q2(LinearTransformationScene):
  def construct(self):
    matrix = [[0, 1], 
              [-1, 0]]
    
    self.add_transformable_mobject(Polygon(np.array([3,-1,0]),np.array([5,-1,0]),np.array([5,2,0]),fill_color=RED, fill_opacity=1, color=RED))
    
    self.add(Dot(np.array([0,0,0]), color=WHITE))
    o = TextMobject("$$(0,1)$$")
    o.move_to(np.array([-1, -0.5, 0]))
    self.play(Write(o))
    
    
    A = TextMobject("$$A$$")
    A.move_to(np.array([2.5,3.5,0]))
    self.play(Write(A))
    
    self.add(Polygon(np.array([3,-1,0]),np.array([5,-1,0]),np.array([5,2,0]),fill_color=RED, fill_opacity=0.5, color=RED))
    self.apply_matrix(matrix)
    A_img = TextMobject("$$A^\prime$$")
  #  A_img.move_to(np.dot(matrix,vector))
    A_img.move_to(np.array([3.5,-1.5,0]))
    self.play(Write(A_img))
    self.wait()
    

class rotation_cw_expl(LinearTransformationScene):
  def construct(self):
    name = TextMobject("Awab Qureshi")
    name.move_to(np.array([-5.5, -3.5, 0]))
    self.add(name)
        
    R_90 = TextMobject("$$90^\circ Clockwise$$")
    R_90.move_to(np.array([-5.5, 2.5, 0]))
    self.add(R_90)
    
    matrix = [[0, 1], 
              [-1, 0]]
    
    self.add_transformable_mobject(Polygon(np.array([2,1,0]),np.array([3,1,0]),np.array([3,3,0]),fill_color=RED, fill_opacity=1, color=RED))
    
    
    A = TextMobject("$$A$$")
    A.move_to(np.array([2.5,3.5,0]))
    self.play(Write(A))
    
    self.add(Polygon(np.array([2,1,0]),np.array([3,1,0]),np.array([3,3,0]),fill_color=RED, fill_opacity=0.5, color=RED))
    self.apply_matrix(matrix)
    A_img = TextMobject("$$A^\prime$$")
  #  A_img.move_to(np.dot(matrix,vector))
    A_img.move_to(np.array([3.5,-1.5,0]))
    self.play(Write(A_img))
    self.add(Polygon(np.array([1,-2,0]),np.array([1,-3,0]),np.array([3,-3,0]),fill_color=RED, fill_opacity=0.5, color=RED))
    self.wait()
    
    R_180 = TextMobject("$$180^\circ Clockwise$$")
    R_180.move_to(np.array([-5.5, 2.5, 0]))
    self.play(Transform(R_90,R_180))
    self.apply_matrix(matrix)
    
    A_img2 = TextMobject("$$A^{\prime\prime}$$")    
    A_img2.move_to(np.array([-3.5,-1.5,0]))
    self.play(Write(A_img2))
    
    self.wait()
    
class rotation_acw_expl(LinearTransformationScene):
  def construct(self):
    name = TextMobject("Awab Qureshi")
    name.move_to(np.array([-5.5, -3.5, 0]))
    self.add(name)
        
    R_90 = TextMobject("$$90^\circ AntiClockwise$$")
    R_90.move_to(np.array([-4.5, 2.5, 0]))
    self.add(R_90)
    
    matrix = [[0, -1], 
              [1, 0]]
    
    self.add_transformable_mobject(Polygon(np.array([2,1,0]),np.array([3,1,0]),np.array([3,3,0]),fill_color=RED, fill_opacity=1, color=RED))
    
    
    A = TextMobject("$$A$$")
    A.move_to(np.array([2.5,3.5,0]))
    self.play(Write(A))
    
    self.add(Polygon(np.array([2,1,0]),np.array([3,1,0]),np.array([3,3,0]),fill_color=RED, fill_opacity=0.5, color=RED))
    self.apply_matrix(matrix)
    A_img = TextMobject("$$A^\prime$$")
  #  A_img.move_to(np.dot(matrix,vector))
    A_img.move_to(np.array([-1.5,3.5,0]))
    self.play(Write(A_img))
    self.add(Polygon(np.array([-1,2,0]),np.array([-1,3,0]),np.array([-3,3,0]),fill_color=RED, fill_opacity=0.5, color=RED))
    self.wait()
    
    R_180 = TextMobject("$$180^\circ AntiClockwise$$")
    R_180.move_to(np.array([-4.5, 2.5, 0]))
    self.play(Transform(R_90,R_180))
    self.apply_matrix(matrix)
    
    A_img2 = TextMobject("$$A^{\prime\prime}$$")    
    A_img2.move_to(np.array([-3.5,-1.5,0]))
    self.play(Write(A_img2))
    
    self.wait()