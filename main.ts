// Entry point for news-image-20261121: copy the front page into /output.
//
// The grader runs this program twice in a fresh container with no network.
// The repository is mounted read-only; /output is writable. The program
// takes the image that sits next to it in the repository and writes the
// exact same bytes to the output directory, so both runs are identical.
import { copyFileSync, existsSync, mkdirSync, statSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const source = join(here, "entry.png");
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const target = join(outDir, "entry.png");

if (!existsSync(source)) {
  throw new Error(`missing entry image: ${source}`);
}
mkdirSync(outDir, { recursive: true });
copyFileSync(source, target);
const bytes = statSync(target).size;
console.log(`wrote ${target} (${bytes} bytes)`);
