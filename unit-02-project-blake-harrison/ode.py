def Euler(diffeq, yn, tn, h):
    """ Given y_n at t, calculate and return y_n+1 at t+h
    """

    #calculate y_n+1
    yn1 = yn + diffeq(yn,tn)*h

    return yn1

def rk2(differeq, yn, tn, h):
    k1 = h * differeq(yn,tn)
    halfstep = differeq(yn+k1/2,tn+h/2)
    k2 = h * halfstep
    yn1 = yn+k2
    
    return yn1

def rk4(differeq, yn, tn, h):
    k1 = h * differeq(yn,tn)
    halfstep = differeq(yn+k1/2,tn+h/2)
    k2 = h * halfstep
    halfstep2 = differeq(yn+k2/2,tn+h/2)
    k3 = h * halfstep2
    halfstep3 = differeq(yn+k3,tn+h)
    k4 = h * halfstep3

    yn1 = yn+(k1/6)+(k2/3)+(k3/3)+(k4/6)
    
    return yn1
    