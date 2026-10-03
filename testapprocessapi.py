from fastapi import FastAPI,Body,Form,UploadFile,File
from pydantic import BaseModel
import uvicorn
app=FastAPI()

class Depts(BaseModel):
    depname:str
    depid:int
    isdepUG:bool

@app.post("/json")
def recjson(dept:Depts):
    return {
        "type":"JSON",
        "depname":dept.depname,
        "depid":dept.depid,
        "depUG":dept.isdepUG
    }

@app.post("/txt")
def rectxt(content:str=Body(...,media_type="text/plain")):
    return {
        "type":"Plain text",
        "content":content
    }

@app.post("/frm")
def recfrm(uname:str=Form(...),upwd:str=Form(...)):
    return{
        "type":"Form Data",
        "username":uname,
        "userpassword":upwd
    }


@app.post("/uploadfile")
def testuploadfile(infile:UploadFile=File(...)):
    return{
        "type":"Upload file",
        "fname":infile.filename,
        "content_type":infile.content_type

    }


if __name__=="__main__":
    uvicorn.run("testapprocessapi:app")
    #uvicorn.run("testapprocessapi:app",host="192.168.1.100",port=8000)

