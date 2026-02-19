import { api } from "src/boot/axios";
import type { GICSResponse, Kpi } from "src/components/models";

export interface ExampleResponse {
  message: string;
}

export async function addKPI(KpiDTO: Kpi): Promise<Kpi> {
  const response = await api.post<Kpi>("kpis/", KpiDTO); // POST
  return response.data;
}

export async function getKPI(): Promise<Kpi[]> {
  const response = await api.get<Kpi[]>("kpis/"); 
  return response.data;
}

export async function fetchExample(): Promise<ExampleResponse> {
  const response = await api.get<ExampleResponse>("example/"); // GET /api/example/
  return response.data;
}

export async function fetchGICS(): Promise<GICSResponse[]> {
  const response = await api.get<GICSResponse[]>("gics/");
  return response.data;
}

export async function fetchGICSIndustryGroups(sector_code: number): Promise<GICSResponse[]> {
  return (await api.get<GICSResponse[]>("gics/industry-groups/", {
    params: {
      sector_code: sector_code,
    }
  })).data;
}

export async function fetchGICSIndustries(industry_group_code: number): Promise<GICSResponse[]> {
  return (await api.get<GICSResponse[]>("gics/industries/", {
    params: {
      industry_group_code: industry_group_code,
    }
  })).data;
}

export async function fetchGICSSubIndustries(industry_code: number): Promise<GICSResponse[]> {
  return (await api.get<GICSResponse[]>("gics/subindustries/", {
    params: {
      industry_code: industry_code,
    }
  })).data;
}