def fibonacci_recursively(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci_recursively(n - 2) + fibonacci_recursively(n - 1)


def fibonacci(n):
    res = [0, 1]
    if 0 <= n < 2:
        return res[n]
    else:
        fb_n, fb_n_1, fb_n_2 = 0, 1, 0
        for i in range(2, n + 1):
            fb_n = fb_n_1 + fb_n_2
            fb_n_2 = fb_n_1
            fb_n_1 = fb_n
        return fb_n


print(fibonacci(7))
