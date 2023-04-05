x = [10,20,30,40,50]
y = [1,2,3,4,5]
m=5
w=5
b=10

w_hist = []
b_hist = []

alpha = 0.001

for i in range(1000000):
    for j in range(m):

        dj_dw = 1/m * (((w*x[j] + b) - y[j]) * x[j])

        dj_db = 1/m * (((w*x[j]) + b) - y[j])

        w = w - alpha * dj_dw
        b = b - alpha * dj_db
        
        if(i%100000==0):
            w_hist.append(w)
            b_hist.append(b)

print("x = [10,20,30,40,50], y = [1,2,3,4,5]\n")
print("w_hist: ", w_hist[-5::])
print("b_hist: ", b_hist[-5::])
print(f"\nw=%f, b=%f"%(w, b))
print(f"\ny=%.2fx+%.2f"%(w,b))
