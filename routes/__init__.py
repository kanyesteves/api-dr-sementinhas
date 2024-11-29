from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

def create_app():
    app = FastAPI()
    origins = ["*"]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )

    from routes import functionRouter
    from routes import presenceRouter
    from routes import userRouter
    from routes import groupRouter
    from routes import priorityRouter
    from routes import eventRouter

    app.include_router(functionRouter.router)
    app.include_router(presenceRouter.router)
    app.include_router(userRouter.router)
    app.include_router(groupRouter.router)
    app.include_router(priorityRouter.router)
    app.include_router(eventRouter.router)

    return app