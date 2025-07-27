import numpy as np

def calculate(inputlist):
    if not type(inputlist) is list:
        raise TypeError('Only list is allowed.')
    if len(inputlist) != 9:
        raise ValueError('List must contain nine numbers.')
    
    mat = np.array(inputlist).reshape(3,3)
    print(mat)
    inputlist = np.array(inputlist)
    print(inputlist)

    axis1 = np.array([mat[:, 0], mat[:, 1], mat[:, 2]])
    axis2 = np.array([mat[0, :], mat[1, :], mat[2, :]])

    calculations = {
        'mean':[list(float(np.mean(_)) for _ in axis1), list(float(np.mean(_)) for _ in axis2), float(np.mean(inputlist))],
        'variance':[list(float(np.var(_)) for _ in axis1), list(float(np.var(_)) for _ in axis2), float(np.var(inputlist))],
        'standard deviation':[list(float(np.std(_)) for _ in axis1),list(float(np.std(_)) for _ in axis2), float(np.std(inputlist))],
        'max':[list(float(np.max(_)) for _ in axis1),list(float(np.max(_)) for _ in axis2), float(np.max(inputlist))],
        'min':[list(float(np.min(_)) for _ in axis1), list(float(np.min(_)) for _ in axis2), float(np.min(inputlist))],
        'sum':[list(float(np.sum(_)) for _ in axis1), list(float(np.sum(_)) for _ in axis2), float(np.sum(inputlist))]
    }
    return calculations