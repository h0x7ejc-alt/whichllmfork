from __future__ import annotations

from dataclasses import dataclass, field

from whichllm.models.types import GGUFVariant, ModelInfo


@dataclass
class ScoreBreakdown:
    benchmark_reference_score: float | None = None
    benchmark_contribution: float = 0.0
    size_contribution: float = 0.0
    quant_penalty: float = 0.0
    evidence_penalty: float = 0.0
    fit_penalty: float = 0.0
    speed_contribution: float = 0.0
    popularity_contribution: float = 0.0
    source_bonus: float = 0.0
    generation_bonus: float = 0.0
    derivative_penalty: float = 0.0
    final_score: float = 0.0


@dataclass
class CompatibilityResult:
    model: ModelInfo
    gguf_variant: GGUFVariant | None
    can_run: bool
    vram_required_bytes: int
    vram_available_bytes: int
    estimated_tok_per_sec: float | None = None
    speed_confidence: str = "medium"
    speed_range_tok_per_sec: tuple[float, float] | None = None
    speed_notes: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    quality_score: float = 0.0
    fit_type: str = "full_gpu"
    benchmark_status: str = "none"
    benchmark_source: str = "none"
    benchmark_confidence: float = 0.0
    score_breakdown: ScoreBreakdown = field(default_factory=ScoreBreakdown)
