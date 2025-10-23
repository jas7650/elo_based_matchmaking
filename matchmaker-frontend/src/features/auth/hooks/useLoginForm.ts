// src/features/auth/hooks/use-login-form.ts
"use client";

import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { loginSchema, type LoginFormValues } from "../schemas/authSchema.ts";

export function useLoginForm() {
  const form = useForm<LoginFormValues>({
    resolver: zodResolver(loginSchema),
    defaultValues: {
      email: "",
      password: "",
    },
  });

  async function onSubmit(values: LoginFormValues) {
    console.log("Submitting login form:", values);
    // Example: Simulate API call
    await new Promise((resolve) => setTimeout(resolve, 1000));
    alert(`Logged in: ${values.email}`);
  }

  return { form, onSubmit };
}
