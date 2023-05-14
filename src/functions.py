
def pulse_eq(y, t, beta, gamma, mu, theta, sigma):
    s, i, v = y
    dsdt = mu - beta * s * i - mu * s + gamma * i + theta * v
    didt = beta * s * i - (gamma + mu) * i + sigma * beta * v * i
    dvdt = - sigma * beta * v * i - (mu + theta) * v
    return dsdt, didt, dvdt
