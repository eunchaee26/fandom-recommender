from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserInput(BaseModel):
    stage: int
    acting: int
    music: int
    voice: int


@app.get("/")
def home():
    return {"message": "Fandom Recommender API Running"}


@app.post("/recommend")
def recommend(data: UserInput):

    scores = {
        "아이돌 덕질형": data.stage,
        "배우 덕질형": data.acting,
        "밴드 덕질형": data.music,
        "솔로가수 덕질형": data.voice
    }

    result = max(scores, key=scores.get)

    descriptions = {
        "아이돌 덕질형":
            "당신은 무대, 예능, 팬 콘텐츠 소비를 즐기는 타입입니다.",

        "배우 덕질형":
            "당신은 작품 감상과 캐릭터 몰입을 좋아하는 타입입니다.",

        "밴드 덕질형":
            "당신은 음악 자체의 완성도를 중요하게 생각합니다.",

        "솔로가수 덕질형":
            "당신은 음색과 감성을 중요하게 생각하는 타입입니다."
    }

    return {
        "result": result,
        "description": descriptions[result]
    }