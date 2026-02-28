import { api } from "src/boot/axios";
import type { GICSResponse, Kpi, kpiToAdd, KpiIndustry, GICSSubindustryAllLayers, KpiIndustryToAdd, KpiIndustryList } from "src/components/models";

export interface ExampleResponse {
  message: string;
}

export async function fetchGICSLayersBySubIndustry(sub_industry_code: number): Promise<GICSSubindustryAllLayers> {
  return (await api.get<GICSSubindustryAllLayers>("gics/get-layers-by-subindustry/", {
    params: {
      sub_industry_code: sub_industry_code,
    }
  })).data;
}

export async function addKPIIndustry(KpiIndustryDTO: KpiIndustryToAdd): Promise<KpiIndustry> {
  const response = await api.post<KpiIndustry>("kpis/industry/", KpiIndustryDTO); 
  return response.data;
}

export async function getAllKPIIndustry(): Promise<KpiIndustryList[]> {
  const response = await api.get<KpiIndustryList[]>("kpis/industry-list/");
  return response.data;
}

export async function addKPI(KpiDTO: kpiToAdd): Promise<Kpi> {
  const response = await api.post<Kpi>("kpis/", KpiDTO); 
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