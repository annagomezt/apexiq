import axios from "axios";

export const api = axios.create({
    baseURL: "https://content-healing-production-5f7c.up.railway.app",
});