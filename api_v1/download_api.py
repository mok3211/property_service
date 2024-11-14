from ..main import app
from fastapi.responses import FileResponse



app.get("/allTasks")
async def getUserAllTask():
    pass


app.get("/download/{task_id}", response_class=FileResponse)
async def download_task_file():
    pass