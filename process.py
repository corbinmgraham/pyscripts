from threading import Thread
import sys

"""
How to use:
    Process Handler
    - Create a custom Thread handler that can take any function
        and that functions arguments
    - Returns nothing but stores the return value of the thread in '.value'
    
    Use: (in path '/') process.py -h OR extension.py
        Running it alone will only run an example, connect it to a project
        to use the Process Handler.
"""

class ProcessHandler(Thread):
  def __init__(self,process,*args):
    Thread.__init__(self)
    self.value = None # Return value
    self.multifunc = process # Process Handler for Function
    self.args=args # Arguments to be passed to function (wrapped)

  def run(self):
    # Unpack and call function with arguments
    self.value = self.multifunc(*self.args)

def example_task(name):
   return f"{name} is running an example task."

def help():
   print("Use: process.py [-h]")

if __name__ == '__main__':
    args = sys.argv
    if(len(args) > 1):
        help()
    else:
        try:
            t = ProcessHandler(example_task, "Example Task")
            t.start() # Start the thread
            t.join() # Wait for thread to finish running
            print(t.value) # Return value of thread
        except:
            print('Fields incorrect.')
            help()
    exit()