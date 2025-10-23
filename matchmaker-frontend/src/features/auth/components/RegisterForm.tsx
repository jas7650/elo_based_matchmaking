import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { FormProvider } from "react-hook-form";
import {
  Field,
  FieldLabel,
  FieldDescription,
  FieldError,
  FieldGroup,
  FieldSet,
} from "@/components/ui/field";
import { useRegisterForm } from "../hooks/useRegisterForm.ts";
import { LogoLink } from "@/components/LogoLink.tsx";

interface RegisterFormProps {
  buttonText?: string;
  googleText?: string;
  loginText?: string;
  loginUrl?: string;
}

const RegisterForm = ({
  buttonText = "Create Account",
  googleText = "Signup with Google",
  loginText = "Already a user?",
  loginUrl = "/login",
}: RegisterFormProps) => {
  const { form, onSubmit } = useRegisterForm();

  return (
    <FormProvider {...form}>
      <form onSubmit={form.handleSubmit(onSubmit)}>
        <section className="bg-background h-screen">
          <div className="flex h-full items-center justify-center">
            <div className="flex flex-col items-center gap-6 lg:justify-start">
              <LogoLink />
              <div className="min-w-sm flex w-full max-w-sm flex-col items-center gap-y-4 rounded-lg border px-6 py-12">
                <Button className="w-full">
                  <img
                    src="https://deifkwefumgah.cloudfront.net/shadcnblocks/block/logos/google-icon.svg"
                    className="mr-2 size-4"
                    alt="Google"
                  />
                  {googleText}
                </Button>

                <div className="relative flex w-full items-center justify-center py-4">
                  <div className="border-border absolute h-[1px] w-full border-t"></div>
                </div>
                <FieldGroup>
                  <FieldSet>
                    <Field data-invalid={!!form.formState.errors.email}>
                      <FieldLabel htmlFor="email">Email</FieldLabel>
                      <Input id="email" placeholder="you@example.com"
                        {...form.register("email")}
                        aria-invalid={!!form.formState.errors.email}
                      />
                      <FieldError>
                        {form.formState.errors.email?.message}
                      </FieldError>
                    </Field>
                    <Field data-invalid={!!form.formState.errors.password}>
                      <FieldLabel htmlFor="password">Password</FieldLabel>
                      <Input id="password" type="password" placeholder="••••••••"
                        {...form.register("password")}
                        aria-invalid={!!form.formState.errors.password}
                      />
                      <FieldError>
                        {form.formState.errors.password?.message}
                      </FieldError>
                    </Field>
                    <Field data-invalid={!!form.formState.errors.passwordConfirm}>
                      <FieldLabel htmlFor="passwordConfirm">Confirm Password</FieldLabel>
                      <Input id="passwordConfirm" type="password" placeholder="••••••••"
                        {...form.register("passwordConfirm")}
                        aria-invalid={!!form.formState.errors.passwordConfirm}
                      />
                      <FieldError>
                        {form.formState.errors.passwordConfirm?.message}
                      </FieldError>
                    </Field>
                  </FieldSet>
                </FieldGroup>
                <Button type="submit" className="w-full" variant="secondary">
                  {buttonText}
                </Button>
              </div>
              <div className="text-muted-foreground flex justify-center gap-1 text-sm">
                <p>{loginText}</p>
                <a
                  href={loginUrl}
                  className="text-primary font-medium hover:underline"
                >
                  Login
                </a>
              </div>
            </div>
          </div>
        </section>
      </form>
    </FormProvider>
  );
};

export { RegisterForm };
