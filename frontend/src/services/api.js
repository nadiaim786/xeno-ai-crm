import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

export const generateCampaign = (
  goal
) =>
  API.post(
    "/campaign/generate",
    { goal }
  );

export const segmentAudience = (
  prompt
) =>
  API.post(
    "/ai/segment",
    { prompt }
  );

export const fetchAnalytics =
  () =>
    API.get(
      "/campaign/analytics"
    );