import axios from "axios";
import type { AxiosInstance } from "axios";
axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

const apiClient: AxiosInstance = axios.create({
  baseURL: "http://localhost:8000/api/", // Django API base
  withCredentials: true,                  // keep cookies/session if you use them
  headers: {
    "Content-Type": "application/json",
  },
});

export default apiClient;