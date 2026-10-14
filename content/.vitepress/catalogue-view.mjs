export function filterTypes(types, filters) {
 return types.filter(type => (!filters.family || type.family === filters.family)
  && (!filters.audience || type.audiences?.includes(filters.audience))
  && (!filters.level || (type.levels || [type.level]).includes(filters.level))
  && (!filters.phase || type.phases?.includes(filters.phase)));
}
