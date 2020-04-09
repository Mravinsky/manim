from manimlib.imports import *
from math import *

#ScaleFaktor = 0.25

class ExampleApproximation(GraphScene):
    CONFIG = {
        "function" : lambda x : np.sin(x),
        "function2" : lambda x : -1*sin(x),  
        "function_color" : BLUE,
        "axes_color":None,
        "x_axis_label": None,
        "y_axis_label": None,
        "taylor" : [lambda x: 2+sin(x), lambda x: 2+sin(x)+1/2*sin(2*x), lambda x: 2+sin(x)+1/2*sin(2*x)+1/3*sin(3*x), lambda x: 2+sin(x)+1/2*sin(2*x)+1/3*sin(3*x)+1/4*sin(4*x), lambda x: 2+sin(x)+1/2*sin(2*x)+1/3*sin(3*x)+1/4*sin(4*x)+1/5*sin(5*x),
        lambda x: 2+sin(x)+1/2*sin(2*x)+1/3*sin(3*x)+1/4*sin(4*x)+1/5*sin(5*x)+1/6*sin(6*x), lambda x: 2+sin(x)+1/2*sin(2*x)+1/3*sin(3*x)+1/4*sin(4*x)+1/5*sin(5*x)+1/6*sin(6*x)+1/7*sin(7*x),
        lambda x: 2+sin(x)+1/2*sin(2*x)+1/3*sin(3*x)+1/4*sin(4*x)+1/5*sin(5*x)+1/6*sin(6*x)+1/7*sin(7*x)+1/8*sin(8*x)],
        "Harmonic1": lambda x: sin(x-pi),
        "Harmonic2": lambda x: sin(x-pi)+1/2*sin(2*x-pi),
        "Harmonic3": lambda x: sin(x-pi)+1/2*sin(2*x-pi)+1/3*sin(3*x-pi),
        "Harmonic4": lambda x: sin(x-pi)+1/2*sin(2*x-pi)+1/3*sin(3*x-pi)+1/4*sin(4*x-pi),
        "Harmonic5": lambda x: sin(x-pi)+1/2*sin(2*x-pi)+1/3*sin(3*x-pi)+1/4*sin(4*x-pi)+1/5*sin(5*x-pi),
        "Harmonic6": lambda x: sin(x-pi)+1/2*sin(2*x-pi)+1/3*sin(3*x-pi)+1/4*sin(4*x-pi)+1/5*sin(5*x-pi)+1/6*sin(6*x-pi),
        "Harmonic7": lambda x: sin(x-pi)+1/2*sin(2*x-pi)+1/3*sin(3*x-pi)+1/4*sin(4*x-pi)+1/5*sin(5*x-pi)+1/6*sin(6*x-pi)+1/7*sin(7*x-pi),
        "Armonicos": [lambda x: sin(x), lambda x: 1/2*sin(2*x), lambda x: 1/3*sin(3*x), lambda x: 1/4*sin(4*x),
        lambda x: 1/5*sin(5*x), lambda x: 1/6*sin(6*x), lambda x: 1/7*sin(7*x), lambda x: 1/8*sin(8*x)],
        "Armonicos2": [lambda x: sin(x-pi), lambda x: sin(x-pi)+1/2*sin(2*x-pi), lambda x: sin(x-pi)+1/2*sin(2*x-pi)+1/3*sin(3*x-pi), 
        lambda x: sin(x-pi)+1/2*sin(2*x-pi)+1/3*sin(3*x-pi)+1/4*sin(4*x-pi), lambda x: sin(x-pi)+1/2*sin(2*x-pi)+1/3*sin(3*x-pi)+1/4*sin(4*x-pi)+1/5*sin(5*x-pi), 
        lambda x: sin(x-pi)+1/2*sin(2*x-pi)+1/3*sin(3*x-pi)+1/4*sin(4*x-pi)+1/5*sin(5*x-pi)+1/6*sin(6*x-pi), 
        lambda x: sin(x-pi)+1/2*sin(2*x-pi)+1/3*sin(3*x-pi)+1/4*sin(4*x-pi)+1/5*sin(5*x-pi)+1/6*sin(6*x-pi)+1/7*sin(7*x-pi), 
        lambda x: sin(x-pi)+1/2*sin(2*x-pi)+1/3*sin(3*x-pi)+1/4*sin(4*x-pi)+1/5*sin(5*x-pi)+1/6*sin(6*x-pi)+1/7*sin(7*x-pi)+1/8*sin(8*x-pi)],
        "ArmonicosPiano": [lambda x: 1/1*sin(1*x-pi), lambda x: 1/1.6304347826087*sin(1.98850574712644*x-pi), lambda x: 1/1.01086956521739*sin(2.98850574712644*x-pi), lambda x: 1/0.614130434782609*sin(3.98850574712644*x-pi), lambda x: 1/1.34782608695652*sin(5*x-pi), lambda x: 1/1.20108695652174*sin(6*x-pi), lambda x: 1/1.30978260869565*sin(7.01149425287356*x-pi), lambda x: 1/1.94565217391304*sin(8.02298850574713*x-pi), 
],
        "ArmonicosPianoSuma": [lambda x: 1/1*sin(1*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.6304347826087*sin(1.98850574712644*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.6304347826087*sin(1.98850574712644*x-pi)+1/1.01086956521739*sin(2.98850574712644*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.6304347826087*sin(1.98850574712644*x-pi)+1/1.01086956521739*sin(2.98850574712644*x-pi)+1/0.614130434782609*sin(3.98850574712644*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.6304347826087*sin(1.98850574712644*x-pi)+1/1.01086956521739*sin(2.98850574712644*x-pi)+1/0.614130434782609*sin(3.98850574712644*x-pi)+1/1.34782608695652*sin(5*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.6304347826087*sin(1.98850574712644*x-pi)+1/1.01086956521739*sin(2.98850574712644*x-pi)+1/0.614130434782609*sin(3.98850574712644*x-pi)+1/1.34782608695652*sin(5*x-pi)+1/1.20108695652174*sin(6*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.6304347826087*sin(1.98850574712644*x-pi)+1/1.01086956521739*sin(2.98850574712644*x-pi)+1/0.614130434782609*sin(3.98850574712644*x-pi)+1/1.34782608695652*sin(5*x-pi)+1/1.20108695652174*sin(6*x-pi)+1/1.30978260869565*sin(7.01149425287356*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.6304347826087*sin(1.98850574712644*x-pi)+1/1.01086956521739*sin(2.98850574712644*x-pi)+1/0.614130434782609*sin(3.98850574712644*x-pi)+1/1.34782608695652*sin(5*x-pi)+1/1.20108695652174*sin(6*x-pi)+1/1.30978260869565*sin(7.01149425287356*x-pi)+1/1.94565217391304*sin(8.02298850574713*x-pi)
],
        "center_point" : 0,
        "h2n_color" : GREEN,
        "h3n_color" : RED,
        "h5n_color" : YELLOW,
        "h7n_color" : PINK,
        "approximation_color" : ORANGE,
        "x_min" : -2*pi,
        "x_max" : 2*pi,
        "y_min" : -6,
        "y_max" : 6,
        "graph_origin" : ORIGIN,
        #"x_labeled_nums" :range(-10,12,2),
    
    }
    def construct(self):
        self.setup_axes(animate=False)

        Armonicos1 = [
            self.get_graph(
                f,
                self.approximation_color,
                x_min=-pi,x_max=pi
            )
            for f in self.Armonicos2
        ]

        sines = VGroup(*[self.get_graph(
            lambda x:np.sin((i+1)*x-pi)*1/(i+1),
            x_min=-pi,x_max=pi
        ) 
            for i in range(8)])
        sines2 = VGroup(*[self.get_graph(
            lambda x:np.sin((i+1)*x-pi)*1/(i+1)*(-1),
            x_min=-pi,x_max=pi
        ) 
            for i in range(8)])
   
        
        Armonicos1a = VGroup(*[
            Armonicos1[0],Armonicos1[1],Armonicos1[2],Armonicos1[3],
            Armonicos1[4],Armonicos1[5],Armonicos1[6],Armonicos1[7],
        ])
        
        sines.set_stroke(opacity=0.95)
        sines2.set_stroke(opacity=0.95)
        
        Armonicos1a.set_stroke(opacity=0.5)  
         
        sines.arrange(UP)  
        sines2.arrange(UP)
        #Armonicos1a.arrange(UP)##########
        Armonicos1a.arrange(
            DOWN,
            #aligned_edge = LEFT,
            buff=-1.45
        )
        Armonicos1a.to_edge(UP)
        sines.to_edge(DOWN)
        sines2.to_edge(DOWN)
        
        self.play(
            ShowCreation(sines, run_time=5),
            ShowCreation(sines2, run_time=5),
            #TransformFromCopy(sines,Armonicos1a, run_time=5)
            ShowCreation(Armonicos1a, run_time=5),
            #rate_func=lambda t: rush_into (t)
            rate_func=lambda t: smooth (t)
        )
        self.wait(2)
        """
        for i in range(len(Armonicos1a)-1):
            self.play(
                ReplacementTransform(Armonicos1a[i],Armonicos1a[i+1]),
                runtime = 0.5
            )
        self.wait()
        """

######################
