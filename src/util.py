from typing import Callable, Any

def force(parser: Callable[..., Any | None]):

    while True:
    
        result = parser()
    
        if result is not None:
        
            return result 
