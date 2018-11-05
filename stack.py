class Stack(object): 

  def __init__(self): 
    """Creates an empty stack """
    self.stack=[] 
    self.size=0 
    self.minimum=None 
  
  def push(self, val):
    """Pushes val on top of stack"""
    self.stack = [val] + self.stack
    self.size += 1 
    self.minimum = min(self.stack) 
  
  def pop(self):
    """If stack is empty, returns False. Else, pops value from top of stack """
    if self.stack == []:
      return False #can't pop empty stack 

    else:
      top = self.stack[0] 
      self.stack = self.stack[1:] 
      self.size -=1 

      if self.stack == []:
        self.minimum=None
      else:
        self.minimum=min(self.stack)

    return top 
  
  def peek(self):
    """Returns top element of stack, false otherwise """
    if self.stack == []:
      return False 
    return self.stack[0] 
  
  def __str__(self):
    if self.stack == []:
      return ""
    output = []
    for element in self.stack:
      output.append(str(element)) 
    return '\n'.join(output); 
  
  def __repr__(self):

    return self.__str__() 
