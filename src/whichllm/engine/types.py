from __future__ import annotations

from dataclasses import dataclass, field

from whichllm.models.types import GGUFVariant, ModelInfo


@dataclass
class CompatibilityResult:
    model: ModelInfo
    gguf_variant: GGUFVariant | None
    can_run: bool
    vram_required_bytes: int
    vram_available_bytes: int
    estimated_tok_per_sec: float | None = None
    speed_confidence: str = "medium"  # "high" | "medium" | "low"
    speed_range_tok_per_sec: tuple[float, float] | None = None
    speed_notes: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    quality_score: float = 0.0  # 0-100 for ranking
    fit_type: str = "full_gpu"  # "full_gpu" | "partial_offload" | "cpu_only"
    benchmark_status: str = "none"  # "direct" | "estimated" | "self_reported" | "none"
    benchmark_source: str = "none"  # granular: "direct" | "variant" | "base_model" | "line_interp" | "self_reported" | "none"
    benchmark_confidence: float = 0.0  # 0.0-1.0 from BenchmarkEvidence

    # Score breakdown fields for --explain
    score_benchmark: float = 0.0
    score_size: float = 0.0
    score_quant_penalty: float = 0.0
    score_evidence_multiplier: float = 1.0
    score_fit_multiplier: float = 1.0
    score_speed: float = 0.0
    score_pop: float = 0.0
    score_source_bonus: float = 0.0
    score_gen_bonus: float = 0.0
    score_derivative_penalty: float = 0.0
    score_quality_core: float = 0.0
