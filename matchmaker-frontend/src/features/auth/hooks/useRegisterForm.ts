// src/features/auth/hooks/use-login-form.ts
"use client";

import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { registerSchema, type RegisterFormValues } from "../schemas/authSchema.ts";

export function useRegisterForm() {
  const form = useForm<RegisterFormValues>({
    resolver: zodResolver(registerSchema),
    defaultValues: {
      email: "",
      password: "",
    },
  });

  async function onSubmit(values: RegisterFormValues) {
    console.log("Submitting register form:", values);
    // Example: Simulate API call
    await new Promise((resolve) => setTimeout(resolve, 1000));
    alert(`Registered: ${values.email}`);
  }

  return { form, onSubmit };
}
