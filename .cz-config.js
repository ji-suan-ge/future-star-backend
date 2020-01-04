module.exports = {
  types: [
    { value: 'Feat', name: 'Feat:     A new feature' },
    { value: 'Fix', name: 'Fix:      A bug fix' },
    { value: 'Docs', name: 'Docs:     Documentation only changes' },
    {
      value: 'Style',
      name:
        'Style:    Changes that do not affect the meaning of the code\n            (white-space, formatting, missing semi-colons, etc)',
    },
    {
      value: 'Refactor',
      name: 'Refactor: A code change that neither fixes a bug nor adds a feature',
    },
    {
      value: 'Perf',
      name: 'Perf:     A code change that improves performance',
    },
    { value: 'Test', name: 'Test:     Adding missing tests' },
    {
      value: 'Chore',
      name:
        'Chore:    Changes to the build process or auxiliary tools\n            and libraries such as documentation generation',
    },
    { value: 'Revert', name: 'Revert:   Revert to a commit' },
    { value: 'WIP', name: 'WIP:      Work in progress' },
  ],
  scopes: [{ name: 'repo' }, { name: 'activity' }, { name: 'administrator' }, { name: 'clazz' },
           { name: 'course' }, { name: 'semester' }, { name: 'student' }, { name: 'util' }, { name: 'config' }],
  allowCustomScopes: false,
  allowBreakingChanges: ['feat', 'fix'],
  subjectLimit: 100,
  ticketNumberPrefix: '',
  footerPrefix : ''
};
