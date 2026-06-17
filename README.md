# devops_repo

A simple REST API built with [FastAPI](https://fastapi.tiangolo.com/) for managing items, backed by an in-memory store.

## Requirements

- Python >= 3.10
- fastapi >= 0.111.0
- uvicorn[standard] >= 0.29.0

## Running the server

* Using pip:

```bash
pip install -r requirements.txt
python3 -m uvicorn main:app --reload --port 8080
```
* Using uv:

```bash
uv sync
uv run uvicorn main:app --reload
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/health` | Health check |
| `GET` | `/items` | List all items |
| `POST` | `/items` | Create a new item |
| `GET` | `/items/{item_id}` | Get an item by ID |
| `DELETE` | `/items/{item_id}` | Delete an item by ID |

Running unit tests:

```
uv sync --group dev
uv run pytest
```

### Item schema

```json
{
  "name": "string",
  "price": 0.0
}
```

## Interactive docs

Once the server is running, visit:
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Registry


* Gitlab repo container registry [https://gitlab.com/dejanualex/devops_demo/container_registry/11708738](https://gitlab.com/dejanualex/devops_demo/container_registry/11708738). Image manifest `registry.example.com/mynamespace/myproject/image:tag` [registry.gitlab.com/dejanualex/devops_demo:latest](registry.gitlab.com/dejanualex/devops_demo:latest)

```
$CI_REGISTRY, $CI_REGISTRY_USER, $CI_REGISTRY_PASSWORD, and $CI_REGISTRY_IMAGE are predefined GitLab CI variables — no setup needed
$CI_REGISTRY_IMAGE resolves to registry.gitlab.com/dejanualex/devops_demo
```
* DockerHub [https://hub.docker.com/r/dejanualex/appserver](https://hub.docker.com/r/dejanualex/appserver)

  - Github tag versioning
  - Gitlab commit sha versioning
