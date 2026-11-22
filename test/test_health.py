
# from fastapi.testclient import TestClient
# from main import app

# client = TestClient(app)


# def test_root():
#     response = client.get("/")
#     assert response.status_code == 200


# def test_health():
#     response = client.get("/api/v1/health")

#     assert response.status_code == 200
#     assert response.json()["status"] == "healthy"


# import numpy as np, xatlas

# v = np.array([[0,0,0],[1,0,0],[0,1,0]], dtype=np.float32)
# f = np.array([[0,1,2]], dtype=np.uint32)
# print(xatlas.parametrize(v, f))

import numpy as np, xatlas
print("numpy", np.__version__, "xatlas imported", flush=True)

v = np.array([[0,0,0],[1,0,0],[0,1,0]], dtype=np.float32)
f = np.array([[0,1,2]], dtype=np.uint32)
print("calling parametrize...", flush=True)
print(xatlas.parametrize(v, f), flush=True)
print("done", flush=True)