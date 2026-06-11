from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class UserInput(BaseModel):
    stage: int
    acting: int
    music: int
    voice: int
    variety: int
    sns: int
    concert: int


@app.get("/")
def root():
    return {"message": "Fandom Recommender API Running"}


@app.post("/recommend")
def recommend(user: UserInput):

    idol_score = user.stage + user.variety + user.sns
    actor_score = user.acting
    band_score = user.music + user.concert
    solo_score = user.voice

    scores = {
        "아이돌 덕질형": idol_score,
        "배우 덕질형": actor_score,
        "밴드 덕질형": band_score,
        "솔로가수 덕질형": solo_score
    }

    result = max(scores, key=scores.get)

    descriptions = {
        "아이돌 덕질형": "당신은 무대, 예능, 팬 콘텐츠를 즐기는 타입입니다.",
        "배우 덕질형": "당신은 연기와 작품 감상을 중요하게 생각하는 타입입니다.",
        "밴드 덕질형": "당신은 음악성과 라이브 공연을 중요하게 생각하는 타입입니다.",
        "솔로가수 덕질형": "당신은 음색과 감성을 중요하게 생각하는 타입입니다."
    }

    return {
        "result": result,
        "description": descriptions[result]
    }