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
import { useLoginForm } from "../hooks/useLoginForm.ts";

interface Login6Props {
  logo: {
    url: string;
    src: string;
    alt: string;
    title?: string;
  };
  buttonText?: string;
  googleText?: string;
  signupText?: string;
  signupUrl?: string;
}

const LoginForm = ({
  logo = {
    url: "https://www.shadcnblocks.com",
    src: "https://deifkwefumgah.cloudfront.net/shadcnblocks/block/logos/shadcnblocks-logo-word.svg",
    alt: "logo",
    title: "shadcnblocks.com",
  },
  buttonText = "Login",
  googleText = "Login with Google",
  signupText = "Need an account?",
  signupUrl = "/register",
}: Login6Props) => {
  const { form, onSubmit } = useLoginForm();

  return (
    <FormProvider {...form}>
      <form onSubmit={form.handleSubmit(onSubmit)}>
        <section className="bg-background h-screen">
          <div className="flex h-full items-center justify-center">
            <div className="flex flex-col items-center gap-6 lg:justify-start">
              {/* Logo */}
              <a href={logo.url}>
                <img
                  src={logo.src}
                  alt={logo.alt}
                  title={logo.title}
                  className="h-10 dark:invert"
                />
              </a>
              <div className="min-w-sm flex w-full max-w-sm flex-col items-center gap-y-4 rounded-lg border px-6 py-12">
                <Button className="w-full">
                  <img
                    src="https://deifkwefumgah.cloudfront.net/shadcnblocks/block/logos/google-icon.svg"
                    className="mr-2 size-4"
                    alt="Google"
                  />
                  {googleText}
                </Button>

                <div className="relative flex w-full items-center justify-center py-2">
                  <div className="border-border absolute h-[1px] w-full border-t"></div>
                  <span className="bg-background text-muted-foreground relative px-2 text-xs">
                    OR
                  </span>
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
                  </FieldSet>
                </FieldGroup>
                <Button type="submit" className="w-full" variant="secondary">
                  {buttonText}
                </Button>
              </div>
              <div className="text-muted-foreground flex justify-center gap-1 text-sm">
                <p>{signupText}</p>
                <a
                  href={signupUrl}
                  className="text-primary font-medium hover:underline"
                >
                  Sign up
                </a>
              </div>
            </div>
          </div>
        </section>
      </form>
    </FormProvider>
  );
};

export { LoginForm };
