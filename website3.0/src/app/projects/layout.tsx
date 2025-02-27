"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import GenLink from "../components/generalLink";

const navLinks = [
    { name: "ASCII Art Generator", href: "/projects/ascii" },
    { name: "Personal Website", href: "/projects/website" },
    { name: "Plant Classifier", href: "/projects/plant-classifier" },
    { name: "Financial Planner", href: "/projects/financial-planner" },
];

export default function ProjectsLayout({ children }: { children: React.ReactNode }) {
    const pathname = usePathname();

    return (
        <div >
            <div>
                {navLinks.map((link) => {
                    const isActive =
                        pathname === link.href || pathname?.startsWith(link.href + "/");

                    return (
                        <GenLink
                            href={link.href}
                            key={link.name}
                            className={`${isActive ? "font-bold text-black mr-4" : "text-blue-500 mr-4"}`}
                        >
                            {link.name}
                        </GenLink>
                    );
                })}
            </div>


            <main>{children}</main>
        </div>
    );
}
