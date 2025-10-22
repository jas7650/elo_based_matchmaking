// src/features/auth/components/RegisterForm.tsx
"use client";

import { FormProvider } from "react-hook-form"; 
// (or just use form.handleSubmit etc)
import {
  Field,
  FieldLabel,
  FieldDescription,
  FieldError,
  FieldGroup,
  FieldSet
} from "@/components/ui/field";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";

import { useNewGroupForm } from "../hooks/useNewGroupForm.ts";

export function NewGroupForm() {
  const { form, onSubmit } = useNewGroupForm();

  return (
    <div>
      <FormProvider {...form}>
        <form onSubmit={form.handleSubmit(onSubmit)} className="max-w-md mx-auto space-y-6 p-6 bg-white rounded-lg shadow">
          {/* Group Name */}
          <FieldGroup>
            <FieldSet>
              <Field data-invalid={!!form.formState.errors.group_name}>
                <FieldLabel htmlFor="group_name">Group Name</FieldLabel>
                <Input id="group_name" placeholder="Group Name"
                  {...form.register("group_name")}
                  aria-invalid={!!form.formState.errors.group_name}
                />
                <FieldDescription>Please enter a group name.</FieldDescription>
                <FieldError>
                  {form.formState.errors.group_name?.message}
                </FieldError>
              </Field>
            </FieldSet>
          </FieldGroup>
          <Button type="submit" className="w-full">Submit</Button>
        </form>
      </FormProvider>
    </div>
  );
}
