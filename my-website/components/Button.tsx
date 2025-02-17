import Link from "next/link";

export default function Button({
    href,
    children,
    className = "",
}: {
    href: string;
    children: React.ReactNode;
    className?: string;
}) {
    return (
        <Link
            href={href}
            className={`rounded border-black/[0.08]
                dark:border-white/[.145]
                transition-colors
                flex items-center
                justify-center
                hover:bg-[#842727]
                dark:hover:bg-[#1a1a1a]
                hover:border-transparent
                text-sm
                sm:text-base
                h-10
                sm:h-12
                px-4
                sm:px-5
                sm:min-w-44
                ${className}`}
        >
            {children}
        </Link>
    );
}
