# Implemetation of SEIR model in Python
## SEIR Model

SEIR model is a variation of the classical SIR model (1927, W.O.Kermack & A.G.McKendrick) to predict the evolution of infectious diseases.
SEIR divides the population of N individuals in 4 classes :
  - Susceptible : for the individuals not yet infected with the disease
  - Exposed : for  individuals who have been infected but are not yet infectious themselves
  - Infectious : for the individuals of the population who have been infected with the disease and are capable of spreading the disease to those in the susceptible category
  - Recovered : for the individuals of the population who have been infected and then removed from the disease, either due to immunization or due to death.
  
  So basically, we have S+E+I+R=N (the sum of the effective of each class is equal to the N individuals, aka the total population).
  
  ## Implementation
  The Model class brings a standalone implementation of the SEIR model.
  It uses the classical set of differential equations for SEIR model (https://wikimedia.org/api/rest_v1/media/math/render/svg/feeb0e885c70ec83c36cec8b33f5ea696f3761a6).
  
  It also comes with a simple GUI for a no-code use and easy to check results :)
  
    
  
