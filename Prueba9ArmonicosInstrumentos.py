from manimlib.imports import *
from math import *

#ScaleFaktor = 0.25

class Piano(GraphScene):
    CONFIG = {
        "function" : lambda x : np.sin(x),
        "function2" : lambda x : -1*sin(x),  
        "function_color" : BLUE,
        "resultante_color" : WHITE,
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
        "ArmonicosPianoFinal": lambda x: 1/1*sin(1*x-pi)+1/1.6304347826087*sin(1.98850574712644*x-pi)+1/1.01086956521739*sin(2.98850574712644*x-pi)+1/0.614130434782609*sin(3.98850574712644*x-pi)+1/1.34782608695652*sin(5*x-pi)+1/1.20108695652174*sin(6*x-pi)+1/1.30978260869565*sin(7.01149425287356*x-pi)+1/1.94565217391304*sin(8.02298850574713*x-pi),

        "ArmonicosGuitarraSuma": [lambda x: 1/1*sin(1*x-pi), lambda x: 1/1*sin(1*x-pi)+1/0.54140127388535*sin(2*x-pi), lambda x: 1/1*sin(1*x-pi)+1/0.54140127388535*sin(2*x-pi)+1/0.917197452229299*sin(3.01149425287356*x-pi), lambda x: 1/1*sin(1*x-pi)+1/0.54140127388535*sin(2*x-pi)+1/0.917197452229299*sin(3.01149425287356*x-pi)+1/1.65605095541401*sin(4.03448275862069*x-pi), lambda x: 1/1*sin(1*x-pi)+1/0.54140127388535*sin(2*x-pi)+1/0.917197452229299*sin(3.01149425287356*x-pi)+1/1.65605095541401*sin(4.03448275862069*x-pi)+1/1.13057324840764*sin(5.03448275862069*x-pi), lambda x: 1/1*sin(1*x-pi)+1/0.54140127388535*sin(2*x-pi)+1/0.917197452229299*sin(3.01149425287356*x-pi)+1/1.65605095541401*sin(4.03448275862069*x-pi)+1/1.13057324840764*sin(5.03448275862069*x-pi)+1/1.29617834394904*sin(6.03448275862069*x-pi), lambda x: 1/1*sin(1*x-pi)+1/0.54140127388535*sin(2*x-pi)+1/0.917197452229299*sin(3.01149425287356*x-pi)+1/1.65605095541401*sin(4.03448275862069*x-pi)+1/1.13057324840764*sin(5.03448275862069*x-pi)+1/1.29617834394904*sin(6.03448275862069*x-pi)+1/1.0859872611465*sin(7.05747126436782*x-pi), lambda x: 1/1*sin(1*x-pi)+1/0.54140127388535*sin(2*x-pi)+1/0.917197452229299*sin(3.01149425287356*x-pi)+1/1.65605095541401*sin(4.03448275862069*x-pi)+1/1.13057324840764*sin(5.03448275862069*x-pi)+1/1.29617834394904*sin(6.03448275862069*x-pi)+1/1.0859872611465*sin(7.05747126436782*x-pi)+1/2.0031847133758*sin(8.04597701149425*x-pi)
],
        "ArmonicosCelloSuma": [lambda x: 1/2*sin(1*x-pi), lambda x: 1/2*sin(1*x-pi)+1/0.48936170212766*sin(2.02298850574713*x-pi), lambda x: 1/2*sin(1*x-pi)+1/0.48936170212766*sin(2.02298850574713*x-pi)+1/1.40425531914894*sin(3.03448275862069*x-pi), lambda x: 1/2*sin(1*x-pi)+1/0.48936170212766*sin(2.02298850574713*x-pi)+1/1.40425531914894*sin(3.03448275862069*x-pi)+1/1.02836879432624*sin(4.04597701149425*x-pi), lambda x: 1/2*sin(1*x-pi)+1/0.48936170212766*sin(2.02298850574713*x-pi)+1/1.40425531914894*sin(3.03448275862069*x-pi)+1/1.02836879432624*sin(4.04597701149425*x-pi)+1/2.07801418439716*sin(5.05747126436782*x-pi), lambda x: 1/2*sin(1*x-pi)+1/0.48936170212766*sin(2.02298850574713*x-pi)+1/1.40425531914894*sin(3.03448275862069*x-pi)+1/1.02836879432624*sin(4.04597701149425*x-pi)+1/2.07801418439716*sin(5.05747126436782*x-pi)+1/2.65248226950355*sin(6.06896551724138*x-pi), lambda x: 1/2*sin(1*x-pi)+1/0.48936170212766*sin(2.02298850574713*x-pi)+1/1.40425531914894*sin(3.03448275862069*x-pi)+1/1.02836879432624*sin(4.04597701149425*x-pi)+1/2.07801418439716*sin(5.05747126436782*x-pi)+1/2.65248226950355*sin(6.06896551724138*x-pi)+1/3.17730496453901*sin(7.08045977011494*x-pi), lambda x: 1/2*sin(1*x-pi)+1/0.48936170212766*sin(2.02298850574713*x-pi)+1/1.40425531914894*sin(3.03448275862069*x-pi)+1/1.02836879432624*sin(4.04597701149425*x-pi)+1/2.07801418439716*sin(5.05747126436782*x-pi)+1/2.65248226950355*sin(6.06896551724138*x-pi)+1/3.17730496453901*sin(7.08045977011494*x-pi)+1/2.97872340425532*sin(8.09195402298851*x-pi)
],
        "ArmonicosPajaroSuma": [lambda x: 1/1*sin(1*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.93636363636364*sin(1.985546875*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.93636363636364*sin(1.985546875*x-pi)+1/1.90909090909091*sin(2.85390625*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.93636363636364*sin(1.985546875*x-pi)+1/1.90909090909091*sin(2.85390625*x-pi)+1/2.79090909090909*sin(3.80078125*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.93636363636364*sin(1.985546875*x-pi)+1/1.90909090909091*sin(2.85390625*x-pi)+1/2.79090909090909*sin(3.80078125*x-pi)+1/3.05909090909091*sin(4.837109375*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.93636363636364*sin(1.985546875*x-pi)+1/1.90909090909091*sin(2.85390625*x-pi)+1/2.79090909090909*sin(3.80078125*x-pi)+1/3.05909090909091*sin(4.837109375*x-pi)+1/3.08181818181818*sin(5.97109375*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.93636363636364*sin(1.985546875*x-pi)+1/1.90909090909091*sin(2.85390625*x-pi)+1/2.79090909090909*sin(3.80078125*x-pi)+1/3.05909090909091*sin(4.837109375*x-pi)+1/3.08181818181818*sin(5.97109375*x-pi)+1/3.17727272727273*sin(6.848828125*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.93636363636364*sin(1.985546875*x-pi)+1/1.90909090909091*sin(2.85390625*x-pi)+1/2.79090909090909*sin(3.80078125*x-pi)+1/3.05909090909091*sin(4.837109375*x-pi)+1/3.08181818181818*sin(5.97109375*x-pi)+1/3.17727272727273*sin(6.848828125*x-pi)+1/2.87272727272727*sin(7.566796875*x-pi)
],
        "ArmonicosPizzicatoSuma": [lambda x: 1/1*sin(1*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.04464285714286*sin(1.96590909090909*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.04464285714286*sin(1.96590909090909*x-pi)+1/1.28125*sin(3.02272727272727*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.04464285714286*sin(1.96590909090909*x-pi)+1/1.28125*sin(3.02272727272727*x-pi)+1/1.73660714285714*sin(4.02272727272727*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.04464285714286*sin(1.96590909090909*x-pi)+1/1.28125*sin(3.02272727272727*x-pi)+1/1.73660714285714*sin(4.02272727272727*x-pi)+1/2.06696428571429*sin(5.05681818181818*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.04464285714286*sin(1.96590909090909*x-pi)+1/1.28125*sin(3.02272727272727*x-pi)+1/1.73660714285714*sin(4.02272727272727*x-pi)+1/2.06696428571429*sin(5.05681818181818*x-pi)+1/2.22767857142857*sin(6.125*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.04464285714286*sin(1.96590909090909*x-pi)+1/1.28125*sin(3.02272727272727*x-pi)+1/1.73660714285714*sin(4.02272727272727*x-pi)+1/2.06696428571429*sin(5.05681818181818*x-pi)+1/2.22767857142857*sin(6.125*x-pi)+1/2.82589285714286*sin(7.25*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.04464285714286*sin(1.96590909090909*x-pi)+1/1.28125*sin(3.02272727272727*x-pi)+1/1.73660714285714*sin(4.02272727272727*x-pi)+1/2.06696428571429*sin(5.05681818181818*x-pi)+1/2.22767857142857*sin(6.125*x-pi)+1/2.82589285714286*sin(7.25*x-pi)+1/2.70982142857143*sin(8.07954545454546*x-pi)
],
        "ArmonicosVozSuma": [lambda x: 1/1*sin(1*x-pi), lambda x: 1/1*sin(1*x-pi)+1/3.62337662337662*sin(1.98265895953757*x-pi), lambda x: 1/1*sin(1*x-pi)+1/3.62337662337662*sin(1.98265895953757*x-pi)+1/1.42857142857143*sin(2.98265895953757*x-pi), lambda x: 1/1*sin(1*x-pi)+1/3.62337662337662*sin(1.98265895953757*x-pi)+1/1.42857142857143*sin(2.98265895953757*x-pi)+1/2.88311688311688*sin(4.00578034682081*x-pi), lambda x: 1/1*sin(1*x-pi)+1/3.62337662337662*sin(1.98265895953757*x-pi)+1/1.42857142857143*sin(2.98265895953757*x-pi)+1/2.88311688311688*sin(4.00578034682081*x-pi)+1/2.85714285714286*sin(4.97687861271676*x-pi), lambda x: 1/1*sin(1*x-pi)+1/3.62337662337662*sin(1.98265895953757*x-pi)+1/1.42857142857143*sin(2.98265895953757*x-pi)+1/2.88311688311688*sin(4.00578034682081*x-pi)+1/2.85714285714286*sin(4.97687861271676*x-pi)+1/3.35064935064935*sin(5.91329479768786*x-pi), lambda x: 1/1*sin(1*x-pi)+1/3.62337662337662*sin(1.98265895953757*x-pi)+1/1.42857142857143*sin(2.98265895953757*x-pi)+1/2.88311688311688*sin(4.00578034682081*x-pi)+1/2.85714285714286*sin(4.97687861271676*x-pi)+1/3.35064935064935*sin(5.91329479768786*x-pi)+1/6.98701298701299*sin(7.05780346820809*x-pi), lambda x: 1/1*sin(1*x-pi)+1/3.62337662337662*sin(1.98265895953757*x-pi)+1/1.42857142857143*sin(2.98265895953757*x-pi)+1/2.88311688311688*sin(4.00578034682081*x-pi)+1/2.85714285714286*sin(4.97687861271676*x-pi)+1/3.35064935064935*sin(5.91329479768786*x-pi)+1/6.98701298701299*sin(7.05780346820809*x-pi)+1/7.76623376623377*sin(7.88439306358381*x-pi)
],
        "ArmonicosTapaSuma": [lambda x: 1/1*sin(1*x-pi), lambda x: 1/1*sin(1*x-pi)+1/8.9344262295082*sin(2.05288461538462*x-pi), lambda x: 1/1*sin(1*x-pi)+1/8.9344262295082*sin(2.05288461538462*x-pi)+1/4.91803278688525*sin(2.70673076923077*x-pi), lambda x: 1/1*sin(1*x-pi)+1/8.9344262295082*sin(2.05288461538462*x-pi)+1/4.91803278688525*sin(2.70673076923077*x-pi)+1/10.6393442622951*sin(3.98918269230769*x-pi), lambda x: 1/1*sin(1*x-pi)+1/8.9344262295082*sin(2.05288461538462*x-pi)+1/4.91803278688525*sin(2.70673076923077*x-pi)+1/10.6393442622951*sin(3.98918269230769*x-pi)+1/8.91803278688525*sin(5.0625*x-pi), lambda x: 1/1*sin(1*x-pi)+1/8.9344262295082*sin(2.05288461538462*x-pi)+1/4.91803278688525*sin(2.70673076923077*x-pi)+1/10.6393442622951*sin(3.98918269230769*x-pi)+1/8.91803278688525*sin(5.0625*x-pi)+1/7.88524590163934*sin(5.82692307692308*x-pi), lambda x: 1/1*sin(1*x-pi)+1/8.9344262295082*sin(2.05288461538462*x-pi)+1/4.91803278688525*sin(2.70673076923077*x-pi)+1/10.6393442622951*sin(3.98918269230769*x-pi)+1/8.91803278688525*sin(5.0625*x-pi)+1/7.88524590163934*sin(5.82692307692308*x-pi)+1/10.655737704918*sin(7.15024038461539*x-pi), lambda x: 1/1*sin(1*x-pi)+1/8.9344262295082*sin(2.05288461538462*x-pi)+1/4.91803278688525*sin(2.70673076923077*x-pi)+1/10.6393442622951*sin(3.98918269230769*x-pi)+1/8.91803278688525*sin(5.0625*x-pi)+1/7.88524590163934*sin(5.82692307692308*x-pi)+1/10.655737704918*sin(7.15024038461539*x-pi)+1/10*sin(7.77644230769231*x-pi)
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
            for f in self.ArmonicosPianoSuma
        ]

        Armonicos2 = [
            self.get_graph(
                f,
                self.resultante_color,
                x_min=-pi,x_max=pi
            )
            for f in self.ArmonicosPianoSuma
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

        Armonicos1c = VGroup(*[
            Armonicos1[0],Armonicos1[1],Armonicos1[2],Armonicos1[3],
            Armonicos1[4],Armonicos1[5],Armonicos1[6],Armonicos2[7],
        ])
        
        sines.set_stroke(opacity=0.35)
        sines2.set_stroke(opacity=0.35)
        
        Armonicos1a.set_stroke(opacity=0.5)  
         
        #sines.arrange(UP)  
        #sines2.arrange(UP)
        #Armonicos1a.arrange(UP)##########
        """
        Armonicos1a.arrange(
            DOWN,
            #aligned_edge = LEFT,
            buff=-4.45
        )"""
        Armonicos1a.to_edge(UP)
        Armonicos1c.to_edge(UP)
        sines.to_edge(DOWN)
        sines2.to_edge(DOWN)
        
        self.play(
            ShowCreation(sines, run_time=2),
            ShowCreation(sines2, run_time=2),
            #TransformFromCopy(sines,Armonicos1a, run_time=5), # Aparecen todos desde abajo
            
            ShowCreation(Armonicos1a, run_time=2),
            #ReplacementTransform(sines,Armonicos1a, run_time=5), # Similar a TransformFromCopy?
            #ShowSubmobjectsOneByOne(Armonicos1a, run_time=5), # Sale de 1 en 1
            
            #ShowIncreasingSubsets(Armonicos1a, run_time=5), # Sale de 1 en 1, pero hasta que termina cada Sines
            #rate_func=lambda t: rush_into (t)
            #Uncreate(Armonicos1a, run_time=5), # Los muestra como ShowCreate y desaparece al final
            #DrawBorderThenFill(Armonicos1a, run_time=5), #Muestra de izquierda a derecha y luego rellena
            rate_func=lambda t: linear (t)
            #rate_func=lambda t: smooth (t) #Primero lewnto y luego rápidop
        )
        #self.wait(2)
        self.play(
            FadeOut(sines2,run_time=2),
            FadeOut(sines,run_time=2),
            ReplacementTransform(Armonicos1a,Armonicos1c[7],run_time=2)
        )
        
        #self.play(FadeOut(sines2))
        #self.play(ReplacementTransform(Armonicos1a,Armonicos1c[7],run_time=2)) #Para que se vea la resultante solamente

        #self.play(TransformFromCopy(Armonicos1a,Armonicos1c[7],run_time=2)) #Para que se vea la resultante 

        self.wait(2)
        #self.play(ShowCreation(Armonicos1a[7]))
        """
        for i in range(len(Armonicos1a)-1):
            self.play(
                ReplacementTransform(Armonicos1a[i],Armonicos1a[i+1]),
                runtime = 0.5
            )
        self.wait()
        """




"""



Separación para la siguiente clase







"""




class Guitarra(GraphScene):
    CONFIG = {
        "function" : lambda x : np.sin(x),
        "function2" : lambda x : -1*sin(x),  
        "function_color" : BLUE,
        "resultante_color" : WHITE,
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
        "ArmonicosPianoFinal": lambda x: 1/1*sin(1*x-pi)+1/1.6304347826087*sin(1.98850574712644*x-pi)+1/1.01086956521739*sin(2.98850574712644*x-pi)+1/0.614130434782609*sin(3.98850574712644*x-pi)+1/1.34782608695652*sin(5*x-pi)+1/1.20108695652174*sin(6*x-pi)+1/1.30978260869565*sin(7.01149425287356*x-pi)+1/1.94565217391304*sin(8.02298850574713*x-pi),

        "ArmonicosGuitarraSuma": [lambda x: 1/1*sin(1*x-pi), lambda x: 1/1*sin(1*x-pi)+1/0.54140127388535*sin(2*x-pi), lambda x: 1/1*sin(1*x-pi)+1/0.54140127388535*sin(2*x-pi)+1/0.917197452229299*sin(3.01149425287356*x-pi), lambda x: 1/1*sin(1*x-pi)+1/0.54140127388535*sin(2*x-pi)+1/0.917197452229299*sin(3.01149425287356*x-pi)+1/1.65605095541401*sin(4.03448275862069*x-pi), lambda x: 1/1*sin(1*x-pi)+1/0.54140127388535*sin(2*x-pi)+1/0.917197452229299*sin(3.01149425287356*x-pi)+1/1.65605095541401*sin(4.03448275862069*x-pi)+1/1.13057324840764*sin(5.03448275862069*x-pi), lambda x: 1/1*sin(1*x-pi)+1/0.54140127388535*sin(2*x-pi)+1/0.917197452229299*sin(3.01149425287356*x-pi)+1/1.65605095541401*sin(4.03448275862069*x-pi)+1/1.13057324840764*sin(5.03448275862069*x-pi)+1/1.29617834394904*sin(6.03448275862069*x-pi), lambda x: 1/1*sin(1*x-pi)+1/0.54140127388535*sin(2*x-pi)+1/0.917197452229299*sin(3.01149425287356*x-pi)+1/1.65605095541401*sin(4.03448275862069*x-pi)+1/1.13057324840764*sin(5.03448275862069*x-pi)+1/1.29617834394904*sin(6.03448275862069*x-pi)+1/1.0859872611465*sin(7.05747126436782*x-pi), lambda x: 1/1*sin(1*x-pi)+1/0.54140127388535*sin(2*x-pi)+1/0.917197452229299*sin(3.01149425287356*x-pi)+1/1.65605095541401*sin(4.03448275862069*x-pi)+1/1.13057324840764*sin(5.03448275862069*x-pi)+1/1.29617834394904*sin(6.03448275862069*x-pi)+1/1.0859872611465*sin(7.05747126436782*x-pi)+1/2.0031847133758*sin(8.04597701149425*x-pi)
],
        "ArmonicosCelloSuma": [lambda x: 1/2*sin(1*x-pi), lambda x: 1/2*sin(1*x-pi)+1/0.48936170212766*sin(2.02298850574713*x-pi), lambda x: 1/2*sin(1*x-pi)+1/0.48936170212766*sin(2.02298850574713*x-pi)+1/1.40425531914894*sin(3.03448275862069*x-pi), lambda x: 1/2*sin(1*x-pi)+1/0.48936170212766*sin(2.02298850574713*x-pi)+1/1.40425531914894*sin(3.03448275862069*x-pi)+1/1.02836879432624*sin(4.04597701149425*x-pi), lambda x: 1/2*sin(1*x-pi)+1/0.48936170212766*sin(2.02298850574713*x-pi)+1/1.40425531914894*sin(3.03448275862069*x-pi)+1/1.02836879432624*sin(4.04597701149425*x-pi)+1/2.07801418439716*sin(5.05747126436782*x-pi), lambda x: 1/2*sin(1*x-pi)+1/0.48936170212766*sin(2.02298850574713*x-pi)+1/1.40425531914894*sin(3.03448275862069*x-pi)+1/1.02836879432624*sin(4.04597701149425*x-pi)+1/2.07801418439716*sin(5.05747126436782*x-pi)+1/2.65248226950355*sin(6.06896551724138*x-pi), lambda x: 1/2*sin(1*x-pi)+1/0.48936170212766*sin(2.02298850574713*x-pi)+1/1.40425531914894*sin(3.03448275862069*x-pi)+1/1.02836879432624*sin(4.04597701149425*x-pi)+1/2.07801418439716*sin(5.05747126436782*x-pi)+1/2.65248226950355*sin(6.06896551724138*x-pi)+1/3.17730496453901*sin(7.08045977011494*x-pi), lambda x: 1/2*sin(1*x-pi)+1/0.48936170212766*sin(2.02298850574713*x-pi)+1/1.40425531914894*sin(3.03448275862069*x-pi)+1/1.02836879432624*sin(4.04597701149425*x-pi)+1/2.07801418439716*sin(5.05747126436782*x-pi)+1/2.65248226950355*sin(6.06896551724138*x-pi)+1/3.17730496453901*sin(7.08045977011494*x-pi)+1/2.97872340425532*sin(8.09195402298851*x-pi)
],
        "ArmonicosPajaroSuma": [lambda x: 1/1*sin(1*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.93636363636364*sin(1.985546875*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.93636363636364*sin(1.985546875*x-pi)+1/1.90909090909091*sin(2.85390625*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.93636363636364*sin(1.985546875*x-pi)+1/1.90909090909091*sin(2.85390625*x-pi)+1/2.79090909090909*sin(3.80078125*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.93636363636364*sin(1.985546875*x-pi)+1/1.90909090909091*sin(2.85390625*x-pi)+1/2.79090909090909*sin(3.80078125*x-pi)+1/3.05909090909091*sin(4.837109375*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.93636363636364*sin(1.985546875*x-pi)+1/1.90909090909091*sin(2.85390625*x-pi)+1/2.79090909090909*sin(3.80078125*x-pi)+1/3.05909090909091*sin(4.837109375*x-pi)+1/3.08181818181818*sin(5.97109375*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.93636363636364*sin(1.985546875*x-pi)+1/1.90909090909091*sin(2.85390625*x-pi)+1/2.79090909090909*sin(3.80078125*x-pi)+1/3.05909090909091*sin(4.837109375*x-pi)+1/3.08181818181818*sin(5.97109375*x-pi)+1/3.17727272727273*sin(6.848828125*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.93636363636364*sin(1.985546875*x-pi)+1/1.90909090909091*sin(2.85390625*x-pi)+1/2.79090909090909*sin(3.80078125*x-pi)+1/3.05909090909091*sin(4.837109375*x-pi)+1/3.08181818181818*sin(5.97109375*x-pi)+1/3.17727272727273*sin(6.848828125*x-pi)+1/2.87272727272727*sin(7.566796875*x-pi)
],
        "ArmonicosPizzicatoSuma": [lambda x: 1/1*sin(1*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.04464285714286*sin(1.96590909090909*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.04464285714286*sin(1.96590909090909*x-pi)+1/1.28125*sin(3.02272727272727*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.04464285714286*sin(1.96590909090909*x-pi)+1/1.28125*sin(3.02272727272727*x-pi)+1/1.73660714285714*sin(4.02272727272727*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.04464285714286*sin(1.96590909090909*x-pi)+1/1.28125*sin(3.02272727272727*x-pi)+1/1.73660714285714*sin(4.02272727272727*x-pi)+1/2.06696428571429*sin(5.05681818181818*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.04464285714286*sin(1.96590909090909*x-pi)+1/1.28125*sin(3.02272727272727*x-pi)+1/1.73660714285714*sin(4.02272727272727*x-pi)+1/2.06696428571429*sin(5.05681818181818*x-pi)+1/2.22767857142857*sin(6.125*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.04464285714286*sin(1.96590909090909*x-pi)+1/1.28125*sin(3.02272727272727*x-pi)+1/1.73660714285714*sin(4.02272727272727*x-pi)+1/2.06696428571429*sin(5.05681818181818*x-pi)+1/2.22767857142857*sin(6.125*x-pi)+1/2.82589285714286*sin(7.25*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.04464285714286*sin(1.96590909090909*x-pi)+1/1.28125*sin(3.02272727272727*x-pi)+1/1.73660714285714*sin(4.02272727272727*x-pi)+1/2.06696428571429*sin(5.05681818181818*x-pi)+1/2.22767857142857*sin(6.125*x-pi)+1/2.82589285714286*sin(7.25*x-pi)+1/2.70982142857143*sin(8.07954545454546*x-pi)
],
        "ArmonicosVozSuma": [lambda x: 1/1*sin(1*x-pi), lambda x: 1/1*sin(1*x-pi)+1/3.62337662337662*sin(1.98265895953757*x-pi), lambda x: 1/1*sin(1*x-pi)+1/3.62337662337662*sin(1.98265895953757*x-pi)+1/1.42857142857143*sin(2.98265895953757*x-pi), lambda x: 1/1*sin(1*x-pi)+1/3.62337662337662*sin(1.98265895953757*x-pi)+1/1.42857142857143*sin(2.98265895953757*x-pi)+1/2.88311688311688*sin(4.00578034682081*x-pi), lambda x: 1/1*sin(1*x-pi)+1/3.62337662337662*sin(1.98265895953757*x-pi)+1/1.42857142857143*sin(2.98265895953757*x-pi)+1/2.88311688311688*sin(4.00578034682081*x-pi)+1/2.85714285714286*sin(4.97687861271676*x-pi), lambda x: 1/1*sin(1*x-pi)+1/3.62337662337662*sin(1.98265895953757*x-pi)+1/1.42857142857143*sin(2.98265895953757*x-pi)+1/2.88311688311688*sin(4.00578034682081*x-pi)+1/2.85714285714286*sin(4.97687861271676*x-pi)+1/3.35064935064935*sin(5.91329479768786*x-pi), lambda x: 1/1*sin(1*x-pi)+1/3.62337662337662*sin(1.98265895953757*x-pi)+1/1.42857142857143*sin(2.98265895953757*x-pi)+1/2.88311688311688*sin(4.00578034682081*x-pi)+1/2.85714285714286*sin(4.97687861271676*x-pi)+1/3.35064935064935*sin(5.91329479768786*x-pi)+1/6.98701298701299*sin(7.05780346820809*x-pi), lambda x: 1/1*sin(1*x-pi)+1/3.62337662337662*sin(1.98265895953757*x-pi)+1/1.42857142857143*sin(2.98265895953757*x-pi)+1/2.88311688311688*sin(4.00578034682081*x-pi)+1/2.85714285714286*sin(4.97687861271676*x-pi)+1/3.35064935064935*sin(5.91329479768786*x-pi)+1/6.98701298701299*sin(7.05780346820809*x-pi)+1/7.76623376623377*sin(7.88439306358381*x-pi)
],
        "ArmonicosTapaSuma": [lambda x: 1/1*sin(1*x-pi), lambda x: 1/1*sin(1*x-pi)+1/8.9344262295082*sin(2.05288461538462*x-pi), lambda x: 1/1*sin(1*x-pi)+1/8.9344262295082*sin(2.05288461538462*x-pi)+1/4.91803278688525*sin(2.70673076923077*x-pi), lambda x: 1/1*sin(1*x-pi)+1/8.9344262295082*sin(2.05288461538462*x-pi)+1/4.91803278688525*sin(2.70673076923077*x-pi)+1/10.6393442622951*sin(3.98918269230769*x-pi), lambda x: 1/1*sin(1*x-pi)+1/8.9344262295082*sin(2.05288461538462*x-pi)+1/4.91803278688525*sin(2.70673076923077*x-pi)+1/10.6393442622951*sin(3.98918269230769*x-pi)+1/8.91803278688525*sin(5.0625*x-pi), lambda x: 1/1*sin(1*x-pi)+1/8.9344262295082*sin(2.05288461538462*x-pi)+1/4.91803278688525*sin(2.70673076923077*x-pi)+1/10.6393442622951*sin(3.98918269230769*x-pi)+1/8.91803278688525*sin(5.0625*x-pi)+1/7.88524590163934*sin(5.82692307692308*x-pi), lambda x: 1/1*sin(1*x-pi)+1/8.9344262295082*sin(2.05288461538462*x-pi)+1/4.91803278688525*sin(2.70673076923077*x-pi)+1/10.6393442622951*sin(3.98918269230769*x-pi)+1/8.91803278688525*sin(5.0625*x-pi)+1/7.88524590163934*sin(5.82692307692308*x-pi)+1/10.655737704918*sin(7.15024038461539*x-pi), lambda x: 1/1*sin(1*x-pi)+1/8.9344262295082*sin(2.05288461538462*x-pi)+1/4.91803278688525*sin(2.70673076923077*x-pi)+1/10.6393442622951*sin(3.98918269230769*x-pi)+1/8.91803278688525*sin(5.0625*x-pi)+1/7.88524590163934*sin(5.82692307692308*x-pi)+1/10.655737704918*sin(7.15024038461539*x-pi)+1/10*sin(7.77644230769231*x-pi)
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
            for f in self.ArmonicosGuitarraSuma
        ]

        Armonicos2 = [
            self.get_graph(
                f,
                self.resultante_color,
                x_min=-pi,x_max=pi
            )
            for f in self.ArmonicosGuitarraSuma
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

        Armonicos1c = VGroup(*[
            Armonicos1[0],Armonicos1[1],Armonicos1[2],Armonicos1[3],
            Armonicos1[4],Armonicos1[5],Armonicos1[6],Armonicos2[7],
        ])
        
        sines.set_stroke(opacity=0.35)
        sines2.set_stroke(opacity=0.35)
        
        Armonicos1a.set_stroke(opacity=0.5)  
         
        #sines.arrange(UP)  
        #sines2.arrange(UP)
        #Armonicos1a.arrange(UP)##########
        """
        Armonicos1a.arrange(
            DOWN,
            #aligned_edge = LEFT,
            buff=-4.45
        )"""
        Armonicos1a.to_edge(UP)
        Armonicos1c.to_edge(UP)
        sines.to_edge(DOWN)
        sines2.to_edge(DOWN)
        
        self.play(
            ShowCreation(sines, run_time=2),
            ShowCreation(sines2, run_time=2),
            #TransformFromCopy(sines,Armonicos1a, run_time=5), # Aparecen todos desde abajo
            
            ShowCreation(Armonicos1a, run_time=2),
            #ReplacementTransform(sines,Armonicos1a, run_time=5), # Similar a TransformFromCopy?
            #ShowSubmobjectsOneByOne(Armonicos1a, run_time=5), # Sale de 1 en 1
            
            #ShowIncreasingSubsets(Armonicos1a, run_time=5), # Sale de 1 en 1, pero hasta que termina cada Sines
            #rate_func=lambda t: rush_into (t)
            #Uncreate(Armonicos1a, run_time=5), # Los muestra como ShowCreate y desaparece al final
            #DrawBorderThenFill(Armonicos1a, run_time=5), #Muestra de izquierda a derecha y luego rellena
            rate_func=lambda t: linear (t)
            #rate_func=lambda t: smooth (t) #Primero lewnto y luego rápidop
        )
        #self.wait(2)
        self.play(
            FadeOut(sines2,run_time=2),
            FadeOut(sines,run_time=2),
            ReplacementTransform(Armonicos1a,Armonicos1c[7],run_time=2)
        )
        
        #self.play(FadeOut(sines2))
        #self.play(ReplacementTransform(Armonicos1a,Armonicos1c[7],run_time=2)) #Para que se vea la resultante solamente

        #self.play(TransformFromCopy(Armonicos1a,Armonicos1c[7],run_time=2)) #Para que se vea la resultante 

        self.wait(2)
        #self.play(ShowCreation(Armonicos1a[7]))
        """
        for i in range(len(Armonicos1a)-1):
            self.play(
                ReplacementTransform(Armonicos1a[i],Armonicos1a[i+1]),
                runtime = 0.5
            )
        self.wait()
        """

######################




"""



Separación para la siguiente clase







"""




class Cello(GraphScene):
    CONFIG = {
        "function" : lambda x : np.sin(x),
        "function2" : lambda x : -1*sin(x),  
        "function_color" : BLUE,
        "resultante_color" : WHITE,
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
        "ArmonicosPianoFinal": lambda x: 1/1*sin(1*x-pi)+1/1.6304347826087*sin(1.98850574712644*x-pi)+1/1.01086956521739*sin(2.98850574712644*x-pi)+1/0.614130434782609*sin(3.98850574712644*x-pi)+1/1.34782608695652*sin(5*x-pi)+1/1.20108695652174*sin(6*x-pi)+1/1.30978260869565*sin(7.01149425287356*x-pi)+1/1.94565217391304*sin(8.02298850574713*x-pi),

        "ArmonicosGuitarraSuma": [lambda x: 1/1*sin(1*x-pi), lambda x: 1/1*sin(1*x-pi)+1/0.54140127388535*sin(2*x-pi), lambda x: 1/1*sin(1*x-pi)+1/0.54140127388535*sin(2*x-pi)+1/0.917197452229299*sin(3.01149425287356*x-pi), lambda x: 1/1*sin(1*x-pi)+1/0.54140127388535*sin(2*x-pi)+1/0.917197452229299*sin(3.01149425287356*x-pi)+1/1.65605095541401*sin(4.03448275862069*x-pi), lambda x: 1/1*sin(1*x-pi)+1/0.54140127388535*sin(2*x-pi)+1/0.917197452229299*sin(3.01149425287356*x-pi)+1/1.65605095541401*sin(4.03448275862069*x-pi)+1/1.13057324840764*sin(5.03448275862069*x-pi), lambda x: 1/1*sin(1*x-pi)+1/0.54140127388535*sin(2*x-pi)+1/0.917197452229299*sin(3.01149425287356*x-pi)+1/1.65605095541401*sin(4.03448275862069*x-pi)+1/1.13057324840764*sin(5.03448275862069*x-pi)+1/1.29617834394904*sin(6.03448275862069*x-pi), lambda x: 1/1*sin(1*x-pi)+1/0.54140127388535*sin(2*x-pi)+1/0.917197452229299*sin(3.01149425287356*x-pi)+1/1.65605095541401*sin(4.03448275862069*x-pi)+1/1.13057324840764*sin(5.03448275862069*x-pi)+1/1.29617834394904*sin(6.03448275862069*x-pi)+1/1.0859872611465*sin(7.05747126436782*x-pi), lambda x: 1/1*sin(1*x-pi)+1/0.54140127388535*sin(2*x-pi)+1/0.917197452229299*sin(3.01149425287356*x-pi)+1/1.65605095541401*sin(4.03448275862069*x-pi)+1/1.13057324840764*sin(5.03448275862069*x-pi)+1/1.29617834394904*sin(6.03448275862069*x-pi)+1/1.0859872611465*sin(7.05747126436782*x-pi)+1/2.0031847133758*sin(8.04597701149425*x-pi)
],
        "ArmonicosCelloSuma": [lambda x: 1/2*sin(1*x-pi), lambda x: 1/2*sin(1*x-pi)+1/0.48936170212766*sin(2.02298850574713*x-pi), lambda x: 1/2*sin(1*x-pi)+1/0.48936170212766*sin(2.02298850574713*x-pi)+1/1.40425531914894*sin(3.03448275862069*x-pi), lambda x: 1/2*sin(1*x-pi)+1/0.48936170212766*sin(2.02298850574713*x-pi)+1/1.40425531914894*sin(3.03448275862069*x-pi)+1/1.02836879432624*sin(4.04597701149425*x-pi), lambda x: 1/2*sin(1*x-pi)+1/0.48936170212766*sin(2.02298850574713*x-pi)+1/1.40425531914894*sin(3.03448275862069*x-pi)+1/1.02836879432624*sin(4.04597701149425*x-pi)+1/2.07801418439716*sin(5.05747126436782*x-pi), lambda x: 1/2*sin(1*x-pi)+1/0.48936170212766*sin(2.02298850574713*x-pi)+1/1.40425531914894*sin(3.03448275862069*x-pi)+1/1.02836879432624*sin(4.04597701149425*x-pi)+1/2.07801418439716*sin(5.05747126436782*x-pi)+1/2.65248226950355*sin(6.06896551724138*x-pi), lambda x: 1/2*sin(1*x-pi)+1/0.48936170212766*sin(2.02298850574713*x-pi)+1/1.40425531914894*sin(3.03448275862069*x-pi)+1/1.02836879432624*sin(4.04597701149425*x-pi)+1/2.07801418439716*sin(5.05747126436782*x-pi)+1/2.65248226950355*sin(6.06896551724138*x-pi)+1/3.17730496453901*sin(7.08045977011494*x-pi), lambda x: 1/2*sin(1*x-pi)+1/0.48936170212766*sin(2.02298850574713*x-pi)+1/1.40425531914894*sin(3.03448275862069*x-pi)+1/1.02836879432624*sin(4.04597701149425*x-pi)+1/2.07801418439716*sin(5.05747126436782*x-pi)+1/2.65248226950355*sin(6.06896551724138*x-pi)+1/3.17730496453901*sin(7.08045977011494*x-pi)+1/2.97872340425532*sin(8.09195402298851*x-pi)
],
        "ArmonicosPajaroSuma": [lambda x: 1/1*sin(1*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.93636363636364*sin(1.985546875*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.93636363636364*sin(1.985546875*x-pi)+1/1.90909090909091*sin(2.85390625*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.93636363636364*sin(1.985546875*x-pi)+1/1.90909090909091*sin(2.85390625*x-pi)+1/2.79090909090909*sin(3.80078125*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.93636363636364*sin(1.985546875*x-pi)+1/1.90909090909091*sin(2.85390625*x-pi)+1/2.79090909090909*sin(3.80078125*x-pi)+1/3.05909090909091*sin(4.837109375*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.93636363636364*sin(1.985546875*x-pi)+1/1.90909090909091*sin(2.85390625*x-pi)+1/2.79090909090909*sin(3.80078125*x-pi)+1/3.05909090909091*sin(4.837109375*x-pi)+1/3.08181818181818*sin(5.97109375*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.93636363636364*sin(1.985546875*x-pi)+1/1.90909090909091*sin(2.85390625*x-pi)+1/2.79090909090909*sin(3.80078125*x-pi)+1/3.05909090909091*sin(4.837109375*x-pi)+1/3.08181818181818*sin(5.97109375*x-pi)+1/3.17727272727273*sin(6.848828125*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.93636363636364*sin(1.985546875*x-pi)+1/1.90909090909091*sin(2.85390625*x-pi)+1/2.79090909090909*sin(3.80078125*x-pi)+1/3.05909090909091*sin(4.837109375*x-pi)+1/3.08181818181818*sin(5.97109375*x-pi)+1/3.17727272727273*sin(6.848828125*x-pi)+1/2.87272727272727*sin(7.566796875*x-pi)
],
        "ArmonicosPizzicatoSuma": [lambda x: 1/1*sin(1*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.04464285714286*sin(1.96590909090909*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.04464285714286*sin(1.96590909090909*x-pi)+1/1.28125*sin(3.02272727272727*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.04464285714286*sin(1.96590909090909*x-pi)+1/1.28125*sin(3.02272727272727*x-pi)+1/1.73660714285714*sin(4.02272727272727*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.04464285714286*sin(1.96590909090909*x-pi)+1/1.28125*sin(3.02272727272727*x-pi)+1/1.73660714285714*sin(4.02272727272727*x-pi)+1/2.06696428571429*sin(5.05681818181818*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.04464285714286*sin(1.96590909090909*x-pi)+1/1.28125*sin(3.02272727272727*x-pi)+1/1.73660714285714*sin(4.02272727272727*x-pi)+1/2.06696428571429*sin(5.05681818181818*x-pi)+1/2.22767857142857*sin(6.125*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.04464285714286*sin(1.96590909090909*x-pi)+1/1.28125*sin(3.02272727272727*x-pi)+1/1.73660714285714*sin(4.02272727272727*x-pi)+1/2.06696428571429*sin(5.05681818181818*x-pi)+1/2.22767857142857*sin(6.125*x-pi)+1/2.82589285714286*sin(7.25*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.04464285714286*sin(1.96590909090909*x-pi)+1/1.28125*sin(3.02272727272727*x-pi)+1/1.73660714285714*sin(4.02272727272727*x-pi)+1/2.06696428571429*sin(5.05681818181818*x-pi)+1/2.22767857142857*sin(6.125*x-pi)+1/2.82589285714286*sin(7.25*x-pi)+1/2.70982142857143*sin(8.07954545454546*x-pi)
],
        "ArmonicosVozSuma": [lambda x: 1/1*sin(1*x-pi), lambda x: 1/1*sin(1*x-pi)+1/3.62337662337662*sin(1.98265895953757*x-pi), lambda x: 1/1*sin(1*x-pi)+1/3.62337662337662*sin(1.98265895953757*x-pi)+1/1.42857142857143*sin(2.98265895953757*x-pi), lambda x: 1/1*sin(1*x-pi)+1/3.62337662337662*sin(1.98265895953757*x-pi)+1/1.42857142857143*sin(2.98265895953757*x-pi)+1/2.88311688311688*sin(4.00578034682081*x-pi), lambda x: 1/1*sin(1*x-pi)+1/3.62337662337662*sin(1.98265895953757*x-pi)+1/1.42857142857143*sin(2.98265895953757*x-pi)+1/2.88311688311688*sin(4.00578034682081*x-pi)+1/2.85714285714286*sin(4.97687861271676*x-pi), lambda x: 1/1*sin(1*x-pi)+1/3.62337662337662*sin(1.98265895953757*x-pi)+1/1.42857142857143*sin(2.98265895953757*x-pi)+1/2.88311688311688*sin(4.00578034682081*x-pi)+1/2.85714285714286*sin(4.97687861271676*x-pi)+1/3.35064935064935*sin(5.91329479768786*x-pi), lambda x: 1/1*sin(1*x-pi)+1/3.62337662337662*sin(1.98265895953757*x-pi)+1/1.42857142857143*sin(2.98265895953757*x-pi)+1/2.88311688311688*sin(4.00578034682081*x-pi)+1/2.85714285714286*sin(4.97687861271676*x-pi)+1/3.35064935064935*sin(5.91329479768786*x-pi)+1/6.98701298701299*sin(7.05780346820809*x-pi), lambda x: 1/1*sin(1*x-pi)+1/3.62337662337662*sin(1.98265895953757*x-pi)+1/1.42857142857143*sin(2.98265895953757*x-pi)+1/2.88311688311688*sin(4.00578034682081*x-pi)+1/2.85714285714286*sin(4.97687861271676*x-pi)+1/3.35064935064935*sin(5.91329479768786*x-pi)+1/6.98701298701299*sin(7.05780346820809*x-pi)+1/7.76623376623377*sin(7.88439306358381*x-pi)
],
        "ArmonicosTapaSuma": [lambda x: 1/1*sin(1*x-pi), lambda x: 1/1*sin(1*x-pi)+1/8.9344262295082*sin(2.05288461538462*x-pi), lambda x: 1/1*sin(1*x-pi)+1/8.9344262295082*sin(2.05288461538462*x-pi)+1/4.91803278688525*sin(2.70673076923077*x-pi), lambda x: 1/1*sin(1*x-pi)+1/8.9344262295082*sin(2.05288461538462*x-pi)+1/4.91803278688525*sin(2.70673076923077*x-pi)+1/10.6393442622951*sin(3.98918269230769*x-pi), lambda x: 1/1*sin(1*x-pi)+1/8.9344262295082*sin(2.05288461538462*x-pi)+1/4.91803278688525*sin(2.70673076923077*x-pi)+1/10.6393442622951*sin(3.98918269230769*x-pi)+1/8.91803278688525*sin(5.0625*x-pi), lambda x: 1/1*sin(1*x-pi)+1/8.9344262295082*sin(2.05288461538462*x-pi)+1/4.91803278688525*sin(2.70673076923077*x-pi)+1/10.6393442622951*sin(3.98918269230769*x-pi)+1/8.91803278688525*sin(5.0625*x-pi)+1/7.88524590163934*sin(5.82692307692308*x-pi), lambda x: 1/1*sin(1*x-pi)+1/8.9344262295082*sin(2.05288461538462*x-pi)+1/4.91803278688525*sin(2.70673076923077*x-pi)+1/10.6393442622951*sin(3.98918269230769*x-pi)+1/8.91803278688525*sin(5.0625*x-pi)+1/7.88524590163934*sin(5.82692307692308*x-pi)+1/10.655737704918*sin(7.15024038461539*x-pi), lambda x: 1/1*sin(1*x-pi)+1/8.9344262295082*sin(2.05288461538462*x-pi)+1/4.91803278688525*sin(2.70673076923077*x-pi)+1/10.6393442622951*sin(3.98918269230769*x-pi)+1/8.91803278688525*sin(5.0625*x-pi)+1/7.88524590163934*sin(5.82692307692308*x-pi)+1/10.655737704918*sin(7.15024038461539*x-pi)+1/10*sin(7.77644230769231*x-pi)
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
            for f in self.ArmonicosCelloSuma
        ]

        Armonicos2 = [
            self.get_graph(
                f,
                self.resultante_color,
                x_min=-pi,x_max=pi
            )
            for f in self.ArmonicosCelloSuma
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

        Armonicos1c = VGroup(*[
            Armonicos1[0],Armonicos1[1],Armonicos1[2],Armonicos1[3],
            Armonicos1[4],Armonicos1[5],Armonicos1[6],Armonicos2[7],
        ])
        
        sines.set_stroke(opacity=0.35)
        sines2.set_stroke(opacity=0.35)
        
        Armonicos1a.set_stroke(opacity=0.5)  
         
        #sines.arrange(UP)  
        #sines2.arrange(UP)
        #Armonicos1a.arrange(UP)##########
        """
        Armonicos1a.arrange(
            DOWN,
            #aligned_edge = LEFT,
            buff=-4.45
        )"""
        Armonicos1a.to_edge(UP)
        Armonicos1c.to_edge(UP)
        sines.to_edge(DOWN)
        sines2.to_edge(DOWN)
        
        self.play(
            ShowCreation(sines, run_time=2),
            ShowCreation(sines2, run_time=2),
            #TransformFromCopy(sines,Armonicos1a, run_time=5), # Aparecen todos desde abajo
            
            ShowCreation(Armonicos1a, run_time=2),
            #ReplacementTransform(sines,Armonicos1a, run_time=5), # Similar a TransformFromCopy?
            #ShowSubmobjectsOneByOne(Armonicos1a, run_time=5), # Sale de 1 en 1
            
            #ShowIncreasingSubsets(Armonicos1a, run_time=5), # Sale de 1 en 1, pero hasta que termina cada Sines
            #rate_func=lambda t: rush_into (t)
            #Uncreate(Armonicos1a, run_time=5), # Los muestra como ShowCreate y desaparece al final
            #DrawBorderThenFill(Armonicos1a, run_time=5), #Muestra de izquierda a derecha y luego rellena
            rate_func=lambda t: linear (t)
            #rate_func=lambda t: smooth (t) #Primero lewnto y luego rápidop
        )
        #self.wait(2)
        self.play(
            FadeOut(sines2,run_time=2),
            FadeOut(sines,run_time=2),
            ReplacementTransform(Armonicos1a,Armonicos1c[7],run_time=2)
        )
        
        #self.play(FadeOut(sines2))
        #self.play(ReplacementTransform(Armonicos1a,Armonicos1c[7],run_time=2)) #Para que se vea la resultante solamente

        #self.play(TransformFromCopy(Armonicos1a,Armonicos1c[7],run_time=2)) #Para que se vea la resultante 

        self.wait(2)
        #self.play(ShowCreation(Armonicos1a[7]))
        """
        for i in range(len(Armonicos1a)-1):
            self.play(
                ReplacementTransform(Armonicos1a[i],Armonicos1a[i+1]),
                runtime = 0.5
            )
        self.wait()
        """

######################




"""



Separación para la siguiente clase







"""




class OtrosPajaroPizzVozTapa(GraphScene):
    CONFIG = {
        "function" : lambda x : np.sin(x),
        "function2" : lambda x : -1*sin(x),  
        "function_color" : BLUE,
        "resultante_color" : WHITE,
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
        "ArmonicosPianoFinal": lambda x: 1/1*sin(1*x-pi)+1/1.6304347826087*sin(1.98850574712644*x-pi)+1/1.01086956521739*sin(2.98850574712644*x-pi)+1/0.614130434782609*sin(3.98850574712644*x-pi)+1/1.34782608695652*sin(5*x-pi)+1/1.20108695652174*sin(6*x-pi)+1/1.30978260869565*sin(7.01149425287356*x-pi)+1/1.94565217391304*sin(8.02298850574713*x-pi),

        "ArmonicosGuitarraSuma": [lambda x: 1/1*sin(1*x-pi), lambda x: 1/1*sin(1*x-pi)+1/0.54140127388535*sin(2*x-pi), lambda x: 1/1*sin(1*x-pi)+1/0.54140127388535*sin(2*x-pi)+1/0.917197452229299*sin(3.01149425287356*x-pi), lambda x: 1/1*sin(1*x-pi)+1/0.54140127388535*sin(2*x-pi)+1/0.917197452229299*sin(3.01149425287356*x-pi)+1/1.65605095541401*sin(4.03448275862069*x-pi), lambda x: 1/1*sin(1*x-pi)+1/0.54140127388535*sin(2*x-pi)+1/0.917197452229299*sin(3.01149425287356*x-pi)+1/1.65605095541401*sin(4.03448275862069*x-pi)+1/1.13057324840764*sin(5.03448275862069*x-pi), lambda x: 1/1*sin(1*x-pi)+1/0.54140127388535*sin(2*x-pi)+1/0.917197452229299*sin(3.01149425287356*x-pi)+1/1.65605095541401*sin(4.03448275862069*x-pi)+1/1.13057324840764*sin(5.03448275862069*x-pi)+1/1.29617834394904*sin(6.03448275862069*x-pi), lambda x: 1/1*sin(1*x-pi)+1/0.54140127388535*sin(2*x-pi)+1/0.917197452229299*sin(3.01149425287356*x-pi)+1/1.65605095541401*sin(4.03448275862069*x-pi)+1/1.13057324840764*sin(5.03448275862069*x-pi)+1/1.29617834394904*sin(6.03448275862069*x-pi)+1/1.0859872611465*sin(7.05747126436782*x-pi), lambda x: 1/1*sin(1*x-pi)+1/0.54140127388535*sin(2*x-pi)+1/0.917197452229299*sin(3.01149425287356*x-pi)+1/1.65605095541401*sin(4.03448275862069*x-pi)+1/1.13057324840764*sin(5.03448275862069*x-pi)+1/1.29617834394904*sin(6.03448275862069*x-pi)+1/1.0859872611465*sin(7.05747126436782*x-pi)+1/2.0031847133758*sin(8.04597701149425*x-pi)
],
        "ArmonicosCelloSuma": [lambda x: 1/2*sin(1*x-pi), lambda x: 1/2*sin(1*x-pi)+1/0.48936170212766*sin(2.02298850574713*x-pi), lambda x: 1/2*sin(1*x-pi)+1/0.48936170212766*sin(2.02298850574713*x-pi)+1/1.40425531914894*sin(3.03448275862069*x-pi), lambda x: 1/2*sin(1*x-pi)+1/0.48936170212766*sin(2.02298850574713*x-pi)+1/1.40425531914894*sin(3.03448275862069*x-pi)+1/1.02836879432624*sin(4.04597701149425*x-pi), lambda x: 1/2*sin(1*x-pi)+1/0.48936170212766*sin(2.02298850574713*x-pi)+1/1.40425531914894*sin(3.03448275862069*x-pi)+1/1.02836879432624*sin(4.04597701149425*x-pi)+1/2.07801418439716*sin(5.05747126436782*x-pi), lambda x: 1/2*sin(1*x-pi)+1/0.48936170212766*sin(2.02298850574713*x-pi)+1/1.40425531914894*sin(3.03448275862069*x-pi)+1/1.02836879432624*sin(4.04597701149425*x-pi)+1/2.07801418439716*sin(5.05747126436782*x-pi)+1/2.65248226950355*sin(6.06896551724138*x-pi), lambda x: 1/2*sin(1*x-pi)+1/0.48936170212766*sin(2.02298850574713*x-pi)+1/1.40425531914894*sin(3.03448275862069*x-pi)+1/1.02836879432624*sin(4.04597701149425*x-pi)+1/2.07801418439716*sin(5.05747126436782*x-pi)+1/2.65248226950355*sin(6.06896551724138*x-pi)+1/3.17730496453901*sin(7.08045977011494*x-pi), lambda x: 1/2*sin(1*x-pi)+1/0.48936170212766*sin(2.02298850574713*x-pi)+1/1.40425531914894*sin(3.03448275862069*x-pi)+1/1.02836879432624*sin(4.04597701149425*x-pi)+1/2.07801418439716*sin(5.05747126436782*x-pi)+1/2.65248226950355*sin(6.06896551724138*x-pi)+1/3.17730496453901*sin(7.08045977011494*x-pi)+1/2.97872340425532*sin(8.09195402298851*x-pi)
],
        "ArmonicosPajaroSuma": [lambda x: 1/1*sin(1*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.93636363636364*sin(1.985546875*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.93636363636364*sin(1.985546875*x-pi)+1/1.90909090909091*sin(2.85390625*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.93636363636364*sin(1.985546875*x-pi)+1/1.90909090909091*sin(2.85390625*x-pi)+1/2.79090909090909*sin(3.80078125*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.93636363636364*sin(1.985546875*x-pi)+1/1.90909090909091*sin(2.85390625*x-pi)+1/2.79090909090909*sin(3.80078125*x-pi)+1/3.05909090909091*sin(4.837109375*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.93636363636364*sin(1.985546875*x-pi)+1/1.90909090909091*sin(2.85390625*x-pi)+1/2.79090909090909*sin(3.80078125*x-pi)+1/3.05909090909091*sin(4.837109375*x-pi)+1/3.08181818181818*sin(5.97109375*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.93636363636364*sin(1.985546875*x-pi)+1/1.90909090909091*sin(2.85390625*x-pi)+1/2.79090909090909*sin(3.80078125*x-pi)+1/3.05909090909091*sin(4.837109375*x-pi)+1/3.08181818181818*sin(5.97109375*x-pi)+1/3.17727272727273*sin(6.848828125*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.93636363636364*sin(1.985546875*x-pi)+1/1.90909090909091*sin(2.85390625*x-pi)+1/2.79090909090909*sin(3.80078125*x-pi)+1/3.05909090909091*sin(4.837109375*x-pi)+1/3.08181818181818*sin(5.97109375*x-pi)+1/3.17727272727273*sin(6.848828125*x-pi)+1/2.87272727272727*sin(7.566796875*x-pi)
],
        "ArmonicosPizzicatoSuma": [lambda x: 1/1*sin(1*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.04464285714286*sin(1.96590909090909*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.04464285714286*sin(1.96590909090909*x-pi)+1/1.28125*sin(3.02272727272727*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.04464285714286*sin(1.96590909090909*x-pi)+1/1.28125*sin(3.02272727272727*x-pi)+1/1.73660714285714*sin(4.02272727272727*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.04464285714286*sin(1.96590909090909*x-pi)+1/1.28125*sin(3.02272727272727*x-pi)+1/1.73660714285714*sin(4.02272727272727*x-pi)+1/2.06696428571429*sin(5.05681818181818*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.04464285714286*sin(1.96590909090909*x-pi)+1/1.28125*sin(3.02272727272727*x-pi)+1/1.73660714285714*sin(4.02272727272727*x-pi)+1/2.06696428571429*sin(5.05681818181818*x-pi)+1/2.22767857142857*sin(6.125*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.04464285714286*sin(1.96590909090909*x-pi)+1/1.28125*sin(3.02272727272727*x-pi)+1/1.73660714285714*sin(4.02272727272727*x-pi)+1/2.06696428571429*sin(5.05681818181818*x-pi)+1/2.22767857142857*sin(6.125*x-pi)+1/2.82589285714286*sin(7.25*x-pi), lambda x: 1/1*sin(1*x-pi)+1/1.04464285714286*sin(1.96590909090909*x-pi)+1/1.28125*sin(3.02272727272727*x-pi)+1/1.73660714285714*sin(4.02272727272727*x-pi)+1/2.06696428571429*sin(5.05681818181818*x-pi)+1/2.22767857142857*sin(6.125*x-pi)+1/2.82589285714286*sin(7.25*x-pi)+1/2.70982142857143*sin(8.07954545454546*x-pi)
],
        "ArmonicosVozSuma": [lambda x: 1/1*sin(1*x-pi), lambda x: 1/1*sin(1*x-pi)+1/3.62337662337662*sin(1.98265895953757*x-pi), lambda x: 1/1*sin(1*x-pi)+1/3.62337662337662*sin(1.98265895953757*x-pi)+1/1.42857142857143*sin(2.98265895953757*x-pi), lambda x: 1/1*sin(1*x-pi)+1/3.62337662337662*sin(1.98265895953757*x-pi)+1/1.42857142857143*sin(2.98265895953757*x-pi)+1/2.88311688311688*sin(4.00578034682081*x-pi), lambda x: 1/1*sin(1*x-pi)+1/3.62337662337662*sin(1.98265895953757*x-pi)+1/1.42857142857143*sin(2.98265895953757*x-pi)+1/2.88311688311688*sin(4.00578034682081*x-pi)+1/2.85714285714286*sin(4.97687861271676*x-pi), lambda x: 1/1*sin(1*x-pi)+1/3.62337662337662*sin(1.98265895953757*x-pi)+1/1.42857142857143*sin(2.98265895953757*x-pi)+1/2.88311688311688*sin(4.00578034682081*x-pi)+1/2.85714285714286*sin(4.97687861271676*x-pi)+1/3.35064935064935*sin(5.91329479768786*x-pi), lambda x: 1/1*sin(1*x-pi)+1/3.62337662337662*sin(1.98265895953757*x-pi)+1/1.42857142857143*sin(2.98265895953757*x-pi)+1/2.88311688311688*sin(4.00578034682081*x-pi)+1/2.85714285714286*sin(4.97687861271676*x-pi)+1/3.35064935064935*sin(5.91329479768786*x-pi)+1/6.98701298701299*sin(7.05780346820809*x-pi), lambda x: 1/1*sin(1*x-pi)+1/3.62337662337662*sin(1.98265895953757*x-pi)+1/1.42857142857143*sin(2.98265895953757*x-pi)+1/2.88311688311688*sin(4.00578034682081*x-pi)+1/2.85714285714286*sin(4.97687861271676*x-pi)+1/3.35064935064935*sin(5.91329479768786*x-pi)+1/6.98701298701299*sin(7.05780346820809*x-pi)+1/7.76623376623377*sin(7.88439306358381*x-pi)
],
        "ArmonicosTapaSuma": [lambda x: 1/1*sin(1*x-pi), lambda x: 1/1*sin(1*x-pi)+1/8.9344262295082*sin(2.05288461538462*x-pi), lambda x: 1/1*sin(1*x-pi)+1/8.9344262295082*sin(2.05288461538462*x-pi)+1/4.91803278688525*sin(2.70673076923077*x-pi), lambda x: 1/1*sin(1*x-pi)+1/8.9344262295082*sin(2.05288461538462*x-pi)+1/4.91803278688525*sin(2.70673076923077*x-pi)+1/10.6393442622951*sin(3.98918269230769*x-pi), lambda x: 1/1*sin(1*x-pi)+1/8.9344262295082*sin(2.05288461538462*x-pi)+1/4.91803278688525*sin(2.70673076923077*x-pi)+1/10.6393442622951*sin(3.98918269230769*x-pi)+1/8.91803278688525*sin(5.0625*x-pi), lambda x: 1/1*sin(1*x-pi)+1/8.9344262295082*sin(2.05288461538462*x-pi)+1/4.91803278688525*sin(2.70673076923077*x-pi)+1/10.6393442622951*sin(3.98918269230769*x-pi)+1/8.91803278688525*sin(5.0625*x-pi)+1/7.88524590163934*sin(5.82692307692308*x-pi), lambda x: 1/1*sin(1*x-pi)+1/8.9344262295082*sin(2.05288461538462*x-pi)+1/4.91803278688525*sin(2.70673076923077*x-pi)+1/10.6393442622951*sin(3.98918269230769*x-pi)+1/8.91803278688525*sin(5.0625*x-pi)+1/7.88524590163934*sin(5.82692307692308*x-pi)+1/10.655737704918*sin(7.15024038461539*x-pi), lambda x: 1/1*sin(1*x-pi)+1/8.9344262295082*sin(2.05288461538462*x-pi)+1/4.91803278688525*sin(2.70673076923077*x-pi)+1/10.6393442622951*sin(3.98918269230769*x-pi)+1/8.91803278688525*sin(5.0625*x-pi)+1/7.88524590163934*sin(5.82692307692308*x-pi)+1/10.655737704918*sin(7.15024038461539*x-pi)+1/10*sin(7.77644230769231*x-pi)
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
            for f in self.ArmonicosPajaroSuma
        ]

        Armonicos2 = [
            self.get_graph(
                f,
                self.resultante_color,
                x_min=-pi,x_max=pi
            )
            for f in self.ArmonicosPajaroSuma
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

        Armonicos1c = VGroup(*[
            Armonicos1[0],Armonicos1[1],Armonicos1[2],Armonicos1[3],
            Armonicos1[4],Armonicos1[5],Armonicos1[6],Armonicos2[7],
        ])
        
        sines.set_stroke(opacity=0.35)
        sines2.set_stroke(opacity=0.35)
        
        Armonicos1a.set_stroke(opacity=0.5)  
         
        #sines.arrange(UP)  
        #sines2.arrange(UP)
        #Armonicos1a.arrange(UP)##########
        """
        Armonicos1a.arrange(
            DOWN,
            #aligned_edge = LEFT,
            buff=-4.45
        )"""
        Armonicos1a.to_edge(UP)
        Armonicos1c.to_edge(UP)
        sines.to_edge(DOWN)
        sines2.to_edge(DOWN)
        
        self.play(
            ShowCreation(sines, run_time=2),
            ShowCreation(sines2, run_time=2),
            #TransformFromCopy(sines,Armonicos1a, run_time=5), # Aparecen todos desde abajo
            
            ShowCreation(Armonicos1a, run_time=2),
            #ReplacementTransform(sines,Armonicos1a, run_time=5), # Similar a TransformFromCopy?
            #ShowSubmobjectsOneByOne(Armonicos1a, run_time=5), # Sale de 1 en 1
            
            #ShowIncreasingSubsets(Armonicos1a, run_time=5), # Sale de 1 en 1, pero hasta que termina cada Sines
            #rate_func=lambda t: rush_into (t)
            #Uncreate(Armonicos1a, run_time=5), # Los muestra como ShowCreate y desaparece al final
            #DrawBorderThenFill(Armonicos1a, run_time=5), #Muestra de izquierda a derecha y luego rellena
            rate_func=lambda t: linear (t)
            #rate_func=lambda t: smooth (t) #Primero lewnto y luego rápidop
        )
        #self.wait(2)
        self.play(
            FadeOut(sines2,run_time=2),
            FadeOut(sines,run_time=2),
            ReplacementTransform(Armonicos1a,Armonicos1c[7],run_time=2)
        )
        
        #self.play(FadeOut(sines2))
        #self.play(ReplacementTransform(Armonicos1a,Armonicos1c[7],run_time=2)) #Para que se vea la resultante solamente

        #self.play(TransformFromCopy(Armonicos1a,Armonicos1c[7],run_time=2)) #Para que se vea la resultante 

        self.wait(2)
        #self.play(ShowCreation(Armonicos1a[7]))
        """
        for i in range(len(Armonicos1a)-1):
            self.play(
                ReplacementTransform(Armonicos1a[i],Armonicos1a[i+1]),
                runtime = 0.5
            )
        self.wait()
        """

######################
