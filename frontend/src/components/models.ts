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

export interface Kpi {
  name: string;
  description: string;
  formula: string;
  unit: string;
  direction: string;
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