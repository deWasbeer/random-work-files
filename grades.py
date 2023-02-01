# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def HnF():
    literatureAndCalculations = 0.
    systemBalances = 0.
    elektrolyserSystemDesign = 0.
    mechanicalComponents = 0.
    strorageTransportAndVariation = 0.
    componentInteraction = 0.
    
    grade = literatureAndCalculations * 0.15 + systemBalances * 0.2 + elektrolyserSystemDesign * 0.15 \
        + mechanicalComponents * 0.2 + strorageTransportAndVariation * 0.15 + componentInteraction * 0.15
    
    return grade

def OwD():
    conceptTurbine = 0.
    prelimTurbine = 0.
    conceptTPMP = 0.
    prelimTPMP = 0.
    prelimPark = 0.
    prelimInstallation = 0.
    
    grade = conceptTurbine * 0.05 + prelimTurbine * 0.2 + conceptTPMP * 0.05 + prelimTPMP * 0.2 + prelimPark * 0.1 + prelimInstallation * 0.15
    
    grade = grade / 0.75
    
    return grade

def waterworld():
    report = 0.
    background = 0.
    OWD = 0.
    ONF = 0.
    TIV = 0.
    HNF = 0.
    
    grade = report * .1 + background * .1 * OWD * .2 + ONF * .2 + TIV * 0.2 + HNF * .2
    
    print('Waterworld grade: ',grade)
    
def deep():
    analyse = 0.
    research = 0.
    design = 0.
    realisation = 0.
    controlling = 0.
    managing = 0.
    advice = 0.
    professionalise = 0.
    
    grade = (analyse + research + design + realisation + controlling + managing + advice + professionalise) / 8.
    
    print('Into the deep grade: ', grade)
    
def main():
    waterworld()
    deep()
main()
