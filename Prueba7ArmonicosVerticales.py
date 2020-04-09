from manimlib.imports import *
from math import *

#ScaleFaktor = 0.25

class ExampleApproximation(GraphScene):
    CONFIG = {
        "color": BLACK,
        "axes_color":None,
        "x_axis_label": None,
        "y_axis_label": None,
        "function" : lambda x : np.sin(x),
        "function2" : lambda x : -1*sin(x),
        "function_color" : BLUE,
        "include_ticks": False,
        "tick_size": 0.1,
        "tick_frequency": 1,
        "taylor" : [lambda x: sin(x), lambda x: sin(x)+1/2*sin(2*x), lambda x: sin(x)+1/2*sin(2*x)+1/3*sin(3*x), lambda x: sin(x)+1/2*sin(2*x)+1/3*sin(3*x)+1/4*sin(4*x), lambda x: sin(x)+1/2*sin(2*x)+1/3*sin(3*x)+1/4*sin(4*x)+1/5*sin(5*x),
        lambda x: sin(x)+1/2*sin(2*x)+1/3*sin(3*x)+1/4*sin(4*x)+1/5*sin(5*x)+1/6*sin(6*x), lambda x: sin(x)+1/2*sin(2*x)+1/3*sin(3*x)+1/4*sin(4*x)+1/5*sin(5*x)+1/6*sin(6*x)+1/7*sin(7*x)],
        "Harmonic1": lambda x: sin(x),
        "Harmonic2": lambda x: 1/2*sin(2*x),
        "Harmonic3": lambda x: 1/3*sin(3*x),
        "Harmonic4": lambda x: 1/4*sin(4*x),
        "Harmonic5": lambda x: 1/5*sin(5*x),
        "Harmonic6": lambda x: 1/6*sin(6*x),
        "Harmonic7": lambda x: 1/7*sin(7*x),
        "center_point" : 0,
        "h2n_color" : GREEN,
        "h3n_color" : RED,
        "h5n_color" : YELLOW,
        "h7n_color" : PINK,
        "approximation_color" : ORANGE,
        "x_min" : 0,
        "x_max" : 2*pi,
        "y_min" : -6,
        "y_max" : 6,
        "graph_origin" : ORIGIN,
        #"x_labeled_nums" :range(-10,12,2),
    
    }
    def construct(self):
        self.setup_axes(animate=False)
        func_graph = self.get_graph(
            self.function,
            self.function_color,
        )
        func_graph2 = self.get_graph(
            self.function2,
            self.function_color,
        )
        approx_graphs = [
            self.get_graph(
                f,
                self.approximation_color,
            )
            for f in self.taylor
        ]
        harmonic_1 = self.get_graph(
                self.Harmonic1,
                self.approximation_color,
        )
        harmonic_2 = self.get_graph(
                self.Harmonic2,
                self.h2n_color,
        )
        harmonic_3 = self.get_graph(
                self.Harmonic3,
                self.h3n_color,
        )
        harmonic_4 = self.get_graph(
                self.Harmonic4,
                self.h2n_color,
        )
        harmonic_5 = self.get_graph(
                self.Harmonic5,
                self.h5n_color,
        )
        harmonic_6 = self.get_graph(
                self.Harmonic6,
                self.h3n_color,
        )
        harmonic_7 = self.get_graph(
                self.Harmonic7,
                self.h7n_color,
        )
        ############ <- Lo chido
        sines = VGroup(*[self.get_graph(
            lambda x:np.sin((i+1)*x-pi)*1/(i+1),
            #lambda x:np.sin((i+1)*x-pi)*1/(i+1)*(-1),
            x_min=-pi,x_max=pi
        ) 
            for i in range(8)])
        
        sines2 = VGroup(*[self.get_graph(
            lambda x:np.sin((i+1)*x-pi)*1/(i+1)*(-1),
            x_min=-pi,x_max=pi
        ) 
            for i in range(8)])
        
        #ListaSenos = [lambda x: sin(x),lambda x: 1/2*sin(2*x),lambda x: 1/3*sin(3*x),
        #lambda x: 1/4*sin(4*x)]
        ########## <- prueba


        ############# <- Acomodo Vertical
        sines.arrange(
            UP,
            #aligned_edge = LEFT,
            #buff=0.4
        )
        sines2.arrange(
            UP,
            #aligned_edge = LEFT,
            #buff=0.4
        )

        
            

        #term_num = [
        #    TexMobject("n = " + str(n),aligned_edge=TOP)
        #    for n in range(0,8)]
        #[t.to_edge(BOTTOM,buff=SMALL_BUFF) for t in term_num]


        #term = TexMobject("")
        #term.to_edge(BOTTOM,buff=SMALL_BUFF)
        
        #approx_graph.to_edge(UP) # No funciona

        self.play(
            ShowCreation(sines, run_time=5),
            ShowCreation(sines2, run_time=5),
            #Transform(approx_graphs[0], approx_graphs[4], run_time = 1),
        )

        self.wait(1)
        
        
        """
        self.play(
            #ShowCreation(harmonic_2),
            Transform(approx_graphs[0], approx_graphs[1], run_time = 1),
        )
        """

        ############

        """
        for n,graph in enumerate(approx_graphs):
            self.play(
                Transform(approx_graph, graph, run_time = 2),
                #Transform(term,term_num[n])
            )
            self.wait()
        """

######################
