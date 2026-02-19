export interface Todo {
  id: number;
  content: string;
}

export interface Meta {
  totalCount: number;
}

export interface GICSResponse {
  code: string;
  name: string;
}

export enum Direction {
  UP = "up",
  DOWN = "down",
  TARGET = "target"
}

export interface Kpi {
  name: string;
  description: string;
  formula: string;
  unit: string;
  direction: Direction;
  frequency: string;
}

export interface KpiIndustry {
  kpi: Kpi;
  sector: GICSResponse;
  industry_group: GICSResponse;
  industry: GICSResponse;
  sub_industry: GICSResponse;
  relevance: string;
}

export interface Benchmark {
  kpi: Kpi;
  sector: GICSResponse;
  industry_group: GICSResponse;
  industry: GICSResponse;
  sub_industry: GICSResponse;
  geography: string;
  company: string;
  period: string;
  value_type: string;
  value_low: string;
  value_high: string;
  source: string;
}