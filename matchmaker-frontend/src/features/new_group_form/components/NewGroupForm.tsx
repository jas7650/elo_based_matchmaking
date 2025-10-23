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
import { LogoLink } from "@/components/LogoLink.tsx";

export function NewGroupForm() {
  const { form, onSubmit } = useNewGroupForm();

  return (
    <FormProvider {...form}>
      <form onSubmit={form.handleSubmit(onSubmit)}>
        <section className="bg-background h-screen">
          <div className="flex h-full items-center justify-center">
            <div className="flex flex-col items-center gap-6 lg:justify-start">
              <LogoLink />
              <div className="min-w-sm flex w-full max-w-sm flex-col items-center gap-y-4 rounded-lg border px-6 py-12">
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
                <Button type="submit" className="w-full">Create Group</Button>
              </div>
            </div>
          </div>
        </section>
      </form>
    </FormProvider>
  );
}
