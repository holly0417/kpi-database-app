export interface Todo {
  id: number;
  content: string;
}

export interface Meta {
  totalCount: number;
}

export interface GICSResponse {
  id: number;
  code: number;
  name: string;
}

export interface GICSSubindustryAllLayers {
  sector: GICSResponse;
  industry_group: GICSResponse;
  industry: GICSResponse;
  sub_industry: GICSResponse;
}

export enum Direction {
  UP = "up",
  DOWN = "down",
  TARGET = "target"
}

export interface kpiToAdd {
  name: string;
  description: string;
  formula: string;
  unit: string;
  direction: Direction;
  frequency: string;
}

export interface Kpi {
  id: number;
  name: string;
  description: string;
  formula: string;
  unit: string;
  direction: Direction;
  frequency: string;
}

export interface KpiIndustryToAdd {
  kpi: number;
  sector: number;
  industry_group: number;
  industry: number;
  sub_industry: number;
}

export interface KpiIndustry {
  id: number;
  kpi: Kpi;
  sector: GICSResponse;
  industry_group: GICSResponse;
  industry: GICSResponse;
  sub_industry: GICSResponse;
}

export interface KpiIndustryList {
  id: number;
  name: string;
  description: string;
  formula: string;
  unit: string;
  direction: Direction;
  frequency: string;
  sector: string;
  industry_group: string;
  industry: string;
  sub_industry: string;
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