
interface LogoLinkProps {
  logo?: {
    url: string;
    src: string;
    alt: string;
    title: string;
  };
}

const LogoLink = ({
  logo = {
    url: "/",
    src: "https://deifkwefumgah.cloudfront.net/shadcnblocks/block/logos/shadcnblockscom-icon.svg",
    alt: "logo",
    title: "PickupManager.com",
  },
}: LogoLinkProps) => {
  return (
    <a href={logo.url} className="flex items-center gap-2">
      <img src={logo.src} className="max-h-8" alt={logo.alt} />
      <span className="text-lg font-semibold tracking-tighter">
        {logo.title}
      </span>
    </a>
  );
};

export { LogoLink };
