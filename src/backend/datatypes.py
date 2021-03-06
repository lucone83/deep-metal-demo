from pydantic import BaseModel, Field

from typing import Dict, List, Optional


class GenerateLyricsRequest(BaseModel):
    text_inputs: Optional[str] = Field(
        "",
        title="Text incipit",
        description="Text incipit (leave empty for unconditioned generation)"
    )
    temperature: Optional[float] = Field(
        1.00,
        title="Temperature",
        description="The value used to module the next token probabilities"
    )


class GenerateLyricsResponse(BaseModel):
    lyrics: List[Dict[str, str]] = Field(
        ...,
        title="Generated lyrics",
        description="Lyrics generated by the model"
    )
