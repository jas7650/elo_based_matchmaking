// src/features/auth/hooks/use-login-form.ts
"use client";

import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { newGroupSchema, type NewGroupFormValues } from "../schemas/newGroupSchema.ts";

export function useNewGroupForm() {
  const form = useForm<NewGroupFormValues>({
    resolver: zodResolver(newGroupSchema),
    defaultValues: {
      group_name: "",
    },
  });

  async function onSubmit(values: NewGroupFormValues) {
    console.log("Submitting login form:", values);
    // Example: Simulate API call
    await new Promise((resolve) => setTimeout(resolve, 1000));
    alert(`Created Group: ${values.group_name}`);
  }

  return { form, onSubmit };
}
