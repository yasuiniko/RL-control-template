from typing import List, NamedTuple
import numpy as np

import jax.numpy as jnp

Batch = NamedTuple('Batch', [
    ('x', np.ndarray),
    ('a', np.ndarray),
    ('xp', np.ndarray),
    ('r', np.ndarray),
    ('gamma', np.ndarray),
])

def getBatchColumns(samples: List):
    cols = list(zip(*samples))

    x = jnp.array(cols[0])
    a = jnp.array(cols[1])
    xp = jnp.array(cols[2])
    r = jnp.array(cols[3])
    gamma = jnp.array(cols[4])

    return Batch(x, a, xp, r, gamma)

def mse_loss(pred: np.ndarray, target: np.ndarray):
    return 0.5 * jnp.mean(jnp.square(pred - target))

def huber_loss(tau: float, pred: np.ndarray, target: np.ndarray):
    diffs = jnp.abs(pred - target)

    quadratic = jnp.minimum(diffs, tau)
    linear = diffs - quadratic

    losses = 0.5 * quadratic**2 + tau * linear

    return jnp.mean(losses)

def takeAlongAxis(a: np.ndarray, ind: np.ndarray):
    return jnp.squeeze(jnp.take_along_axis(a, ind[..., None], axis=-1), axis=-1)
