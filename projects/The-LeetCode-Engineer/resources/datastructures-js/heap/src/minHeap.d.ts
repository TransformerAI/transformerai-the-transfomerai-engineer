import { Heap } from "./heap";
import { IGetCompareValue } from "./maxHeap";

export class MinHeap<T> implements Iterable<T> {
  constructor(getCompareValue?: IGetCompareValue<T>, _heap?: Heap<T>);
  toArray(): T[];
  [Symbol.iterator](): Iterator<T, any, undefined>;
  insert(value: T): MinHeap<T>;
  push(value: T): MinHeap<T>;
  extractRoot(): T | null;
  pop(): T | null;
  sort(): T[];
  fix(): MinHeap<T>;
  isValid(): boolean;
  clone(): MinHeap<T>;
  root(): T | null;
  top(): T | null;
  leaf(): T | null;
  size(): number;
  isEmpty(): boolean;
  clear(): void;
  static heapify<T>(
    values: T[],
    getCompareValue?: IGetCompareValue<T>
  ): MinHeap<T>;
  static isHeapified<T>(
    values: T[],
    getCompareValue?: IGetCompareValue<T>
  ): boolean;
}
