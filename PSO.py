import math
"""
La clase Rnd simula la generación de números
aleatorios. En este caso, de implementan los 
del ejercicio. Se separó en 2:
a) Los aleatorios binarios, para la inicialización
de las posiciones (x) de las partículas
b) Los aleatorios reales para los elementos: epsilon 
1 y 2, y para el r de la sigmoide.
"""


class Rnd:

  binary = [
      1,0,0,0,0,0,
      0,1,1,0,0,0,
      1,1,0,1,0,0,
      0,1,1,0,1,0,
      1,0,1,1,0,0,
  ]

  real = [
      0.37, 0.33, 0.35, 0.96, 0.31, 0.98, 0.39, 0.0, 0.19, 0.02, 0.75, 0.79,
      0.04, 0.65, 0.6, 0.96, 0.56, 0.99, 0.72, 0.48, 0.4, 0.96, 0.22, 0.73,
      0.88, 0.66, 0.22, 0.0, 0.87, 0.12, 0.74, 0.52, 0.74, 0.02, 0.67, 0.61,
      0.03, 0.21, 0.31, 0.56, 0.41, 0.76, 0.59, 0.83, 0.96, 0.76, 0.5, 0.33,
      0.42, 0.59, 0.09, 0.15, 0.91, 0.65, 0.38, 0.52, 0.56, 0.84, 0.74, 0.6,
      0.08, 0.64, 0.47, 0.75, 0.67, 0.55, 0.72, 0.32, 0.75, 0.17, 0.99, 0.64,
      0.49, 0.04, 0.42, 0.77, 0.17, 0.57, 0.33, 0.96, 0.90, 0.74, 0.65, 0.12,
      0.63, 0.25, 0.53, 0.36, 0.85, 0.08, 0.19, 0.69, 0.79, 0.93, 0.88, 0.29,
      0.09, 0.67, 0.9, 0.82, 0.77, 0.4, 0.47, 0.53, 0.03, 0.45, 0.91, 0.5,
      0.23, 0.46, 0.95, 0.07, 0.23, 0.8, 0.62, 0.35, 0.1, 0.2, 0.58, 0.88,
      0.85, 0.9, 0.57, 0.95, 0.13, 0.9, 0.72, 0.77, 0.67, 0.01, 0.49, 0.46,
      0.46, 0.43, 0.41, 0.55, 0.61, 0.51, 0.17, 0.57, 0.83, 0.75, 0.95, 0.45,
      0.3, 0.43, 0.53, 0.99, 0.22, 0.15, 0.92, 0.29, 0.91, 0.36, 0.06, 0.17,
      0.28, 0.49, 0.88, 0.15, 0.52, 0.95, 0.85, 0.33, 0.28, 0.25, 0.05, 0.18,
      0.9, 0.56, 0.05, 0.24, 0.47, 0.54, 0.79, 0.44, 0.24, 0.5, 0.7, 0.96,
      0.07, 0.99, 0.33, 0.7, 0.35, 0.25, 0.3, 0.96, 0.38, 0.98, 0.87, 0.53,
      0.13, 0.72, 0.52, 0.71, 0.1, 0.79, 0.74, 0.91, 0.79, 0.65, 0.5, 0.72,
      0.69, 0.07, 0.27, 0.39, 0.04, 0.72, 0.97, 0.81, 0.82, 0.96, 0.27, 0.53,
      0.93, 0.58, 0.96, 0.42, 0.94, 0.74, 0.08, 0.51, 0.56, 0.23, 0.66, 0.3,
      0.73, 0.02, 0.73, 0.48, 0.51, 0.92, 0.2, 0.5, 0.6, 0.61, 0.5, 0.17, 0.82,
      0.71, 0.13, 0.38, 0.96, 0.65, 0.89, 0.45, 0.84, 0.51, 0.19, 0.4, 0.21,
      0.39, 0.7, 0.9, 0.14, 0.35, 0.99, 0.68, 0.27, 0.14, 0.56, 0.23, 0.49,
      0.24, 0.33, 0.17, 0.22, 0.31, 0.11, 0.23, 0.95, 0.15, 0.13, 0.27, 0.45,
      0.07, 0.39, 0.32, 0.12, 0.69, 0.27, 0.86, 0.1, 0.46, 0.34, 0.2, 0.03,
      0.7, 0.83, 0.95, 0.95, 0.79, 0.22, 0.98, 0.33, 0.02, 0.34, 0.59, 0.24,
      0.78, 0.84, 0.58, 0.09, 0.68, 0.04, 0.49, 0.19, 0.29, 0.75, 0.91, 0.12,
      0.62, 0.15, 0.67, 0.15, 0.87, 0.88, 0.52, 0.5, 0.26, 0.39, 0.78, 0.88,
      0.91, 0.02, 0.29, 0.65, 0.88, 0.49, 0.56, 0.98, 0.44, 0.5, 0.96, 0.23,
      0.27, 0.67, 0.86, 0.67, 0.96, 0.45, 0.39, 0.3, 0.11, 0.27, 0.79, 0.71,
      0.02, 0.92, 0.34, 0.7, 0.58, 0.79, 0.02, 0.79, 0.84, 0.96, 0.74, 0.86,
      0.19, 0.87, 0.01, 0.66, 0.28, 0.44, 0.62, 0.66, 0.38, 0.88, 0.62, 0.96,
      0.06, 0.53, 0.1, 0.77, 0.69, 0.43, 0.51, 0.6, 0.28, 0.31, 0.54, 0.21,
      0.54, 0.44, 0.6, 0.3, 0.81, 0.86, 0.59, 0.14, 0.43, 0.27, 0.92, 0.1,
      0.27, 0.36, 0.12, 0.29, 0.52, 0.05, 0.22, 0.34, 0.49, 0.5, 0.58, 0.98,
      0.64, 0.52, 0.72, 0.35, 0.77, 0.42, 0.49, 0.5, 0.52, 0.92, 0.3, 0.14,
      0.33, 0.89, 0.0, 0.69, 0.29, 0.08, 0.51, 0.37, 0.49, 0.18, 0.6, 0.36,
      0.12, 0.31, 0.9, 0.12, 0.51, 0.28, 0.55, 0.52, 0.03, 0.82, 0.17, 0.64,
      0.43, 0.35
  ]

  rndBinaryCont = -1
  rndRealCont = -1

  @staticmethod
  def random_binary():
    Rnd.rndBinaryCont += 1
    return Rnd.binary[Rnd.rndBinaryCont % len(Rnd.binary)]

  @staticmethod
  def random_real():
    Rnd.rndRealCont += 1
    return Rnd.real[Rnd.rndRealCont % len(Rnd.real)]


"""
La clase Problem implementa el problema a resolver.
Tiene el atributo nVars, que representa la dimensión 
(cantidad de variables de decisión)
Tiene el método check_constraint que verifica que la 
solución cumple con la restricción.
Tiene el método compute_fitness que regresa el valor
o calidad de la solución (función objetivo).
"""


class Problem:

  nVars = 6
  capital_inicial = 1200  # Capital inicial disponible
  costos = [200, 150, 350, 250, 300, 400]  # Costos de inversión (Cj)
  rois = [150, 180, 120, 160, 140, 170]  # Retornos de inversión (ROIj)

  @staticmethod
  def check_constraint(x):
    total_cost = sum(Problem.costos[i] * x[i] for i in range(Problem.nVars))
    return total_cost <= Problem.capital_inicial

  @staticmethod
  def compute_fitness(x):
    total_roi = sum(Problem.rois[i] * x[i] for i in range(Problem.nVars))
    return total_roi


class Particle:

  def __init__(self, init=True):
    self.x = [Rnd.random_binary()
              for _ in range(Problem.nVars)] if init else []
    self.v = [0 for _ in range(Problem.nVars)] if init else []
    self.p = self.x.copy() if init else []

  def update_p(self):
    self.p = self.x.copy()

  def is_feasible(self):
    return Problem.check_constraint(self.x)

  def fitness(self):
    return Problem.compute_fitness(self.x)

  def fitness_p(self):
    return Problem.compute_fitness(self.p)

  def is_better_than_p(self):
    return self.fitness() > self.fitness_p()

  def is_better_than(self, g):
    return self.fitness() > g.fitness_p()

  def move(self, g, w, alpha, beta):
    for j in range(Problem.nVars):
      self.v[j] = (self.v[j] * w + alpha * Rnd.random_real() *
                   (g.p[j] - self.x[j]) + beta * Rnd.random_real() *
                   (self.p[j] - self.x[j]))

      self.x[j] = self.to_binary(self.v[j])

  def to_binary(self, v):
    return 1 if (1 / (1 + math.exp(-v))) > Rnd.random_real() else 0

  def copy(self, other):
    if isinstance(other, Particle):
      self.x = other.x.copy()
      self.p = other.p.copy()
      self.v = other.v.copy()

  def __str__(self):
    return f"v: {self.v}, x: {self.x}, p: {self.p}, fitness {self.fitness_p()}"


class PSO:

  def __init__(self):
    self.popSize = 5
    self.T = 5
    self.w = 0.9
    self.alpha = 0.6
    self.beta = 0.6
    self.swarm = []
    self.g = None

  def solve(self):
    self.init_random()
    self.evolve()

  def init_random(self):
    self.g = Particle(False)
    for _ in range(self.popSize):
      while True:
        p_aux = Particle()
        if p_aux.is_feasible():
          break
      self.swarm.append(p_aux)

    self.g.copy(self.swarm[0])
    for i in range(self.popSize):
      if self.swarm[i].is_better_than(self.g):
        self.g.copy(self.swarm[i])

  def evolve(self):
    self.show_results(0)
    t = 1
    while t <= self.T:
      for i in range(self.popSize):
        p_aux = Particle(False)
        p_aux.copy(self.swarm[i])
        while True:
          p_aux.move(self.g, self.w, self.alpha, self.beta)
          if p_aux.is_feasible():
            break
        self.swarm[i].copy(p_aux)

      for i in range(self.popSize):
        if self.swarm[i].is_better_than_p():
          self.swarm[i].update_p()
        if self.swarm[i].is_better_than(self.g):
          self.g.copy(self.swarm[i])

      self.show_results(t)
      t += 1

  def show_results(self, t):
    print(f"Iteration: {t}")
    for i in range(self.popSize):
      print(f"Particle {i+1}: {self.swarm[i]}")
    print(f"GlobalBest: {self.g}\n")


class Main:

  @staticmethod
  def main():
    try:
      PSO().solve()
    except Exception as e:
      print(f"Error: {e}")


if __name__ == "__main__":
  Main.main()
