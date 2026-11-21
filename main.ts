// main.ts — make.fun news-image entry (Node 22, standard library only).
// The entry image is the entry.png shipped beside this file. This program
// copies it, byte for byte, to the grader's output directory. It uses no
// network and no randomness, so repeated runs produce identical bytes.
//
// Local run:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
import { copyFileSync, mkdirSync, statSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const repoRoot = dirname(fileURLToPath(import.meta.url));
const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const source = join(repoRoot, "entry.png");
const target = join(outputDir, "entry.png");

mkdirSync(outputDir, { recursive: true });
copyFileSync(source, target);
// The entry must be byte-identical on every run: refuse a partial copy.
const sourceBytes = statSync(source).size;
const targetBytes = statSync(target).size;
if (sourceBytes !== targetBytes) {
  throw new Error(`entry.png copy incomplete: ${targetBytes} of ${sourceBytes} bytes`);
}
console.log(`wrote ${target} (${targetBytes} bytes)`);
