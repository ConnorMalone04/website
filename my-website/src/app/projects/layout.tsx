"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

const navLinks = [
    { name: "Personal Website", href: "/projects/website" },
    { name: "Plant Classifier", href: "/projects/plant-classifier" },
    { name: "Financial Planner", href: "/projects/financial-planner" },
];

export default function ProjectsLayout({ children }: { children: React.ReactNode }) {
    const pathname = usePathname();

    return (
        <div>
            {navLinks.map((link) => {
                const isActive =
                    pathname === link.href || pathname?.startsWith(link.href + "/");

                return (
                    <Link
                        href={link.href}
                        key={link.name}
                        className={isActive ? "font-bold text-black mr-4" : "text-blue-500 mr-4"}
                    >
                        {link.name}
                    </Link>
                );
            })}


            <main>{children}</main>
        </div>
    );
}
