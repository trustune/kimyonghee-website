library(pscl)
library(MASS)

# Synthetic data
set.seed(42)
n <- 200
x1 <- rnorm(n)
x2 <- rbinom(n, 1, 0.5)
z_prob <- 1 / (1 + exp(-(-1 + x2)))
is_zero <- rbinom(n, 1, z_prob)
lam <- exp(1 + 0.5*x1)
counts <- rpois(n, lam)
y <- counts * (1 - is_zero)
df <- data.frame(y=y, x1=x1, x2=x2)

# Models
m1 <- glm(y ~ x1, data=df, family=poisson)
m2 <- zeroinfl(y ~ x1 | x2, data=df, dist="poisson")

# Vuong test
print("Running Vuong test...")
v <- vuong(m1, m2)
print(class(v))
print(v)

if (is.null(v)) {
    print("Vuong result is NULL")
} else {
    print("Vuong result is NOT NULL")
    print(v@test_stat)
}
