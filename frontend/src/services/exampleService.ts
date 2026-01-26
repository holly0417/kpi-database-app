import apiClient from "./api";
import type { GICSResponse } from "src/components/models";

export interface ExampleResponse {
  message: string;
}

export async function fetchExample(): Promise<ExampleResponse> {
  const response = await apiClient.get<ExampleResponse>("example/"); // GET /api/example/
  return response.data;
}

export async function fetchGICS(): Promise<GICSResponse[]> {
  const response = await apiClient.get<GICSResponse[]>("gics/");
  return response.data;
}